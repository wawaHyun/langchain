from dataclasses import dataclass


@dataclass
class TitanicModel:
    context : str
    fname : str
    train : object
    test : object
    id : str
    label : str

@property
def context(self) -> str: return self.context

@context.setter
def context(self, context: str): self.context = context

@property
def fname(self) -> str: return self.fname

@context.setter
def fname(self, fname: str): self.fname = fname

@property
def train(self) -> object: return self.train

@context.setter
def train(self, train: object): self.train = train

@property
def test(self) -> object: return self.test

@context.setter
def test(self, test: object): self.test = test

@property
def id(self) -> str: return self.id

@context.setter
def id(self, id: str): self.id = id

@property
def label(self) -> str: return self.label

@context.setter
def label(self, label: str): self.label = label

