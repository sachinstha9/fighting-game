import random
import torch
import torch.nn as nn
import torch.optim as optim
from model import Qnet

device = "cuda" if torch.cuda.is_available() else "cpu"

class Agent:
    def __init__(self):
        self.model = Qnet().to(device)
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)

        self.gamma = 0.9
        self.epsilon = 1
        self.epsilon_decay = 0.995
        self.min_epsilon = 0

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 4)
        
        state = torch.tensor(state, dtype=torch.float32).unsqueeze(0).to(device)

        with torch.no_grad():
            q = self.model(state)

        return torch.argmax(q).item()

    def train(self, state, next_state, done, action, reward, epsilon_update=True):
        state = torch.tensor(state, dtype=torch.float32).unsqueeze(0).to(device)
        next_state = torch.tensor(next_state, dtype=torch.float32).unsqueeze(0).to(device)

        q_values = self.model(state)
        next_q = self.model(next_state)

        target = q_values.clone().detach()

        if done:
            target[0, action] = reward
        else:
            target[0, action] = reward + self.gamma * torch.max(next_q)

        loss = nn.SmoothL1Loss()(q_values, target)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        if self.epsilon > self.min_epsilon and epsilon_update:
            self.epsilon *= self.epsilon_decay
            print(self.epsilon)