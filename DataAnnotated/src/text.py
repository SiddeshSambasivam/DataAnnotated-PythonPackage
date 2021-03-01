from ..Utils.utils import log

class TextEntityAnnotation:

    def __init__(self, user_dataset):

        self.dataset = user_dataset['raw_data']+user_dataset['annotated_data']
        self.task_id = user_dataset['task_id']
        self.task_name = user_dataset['task_name']
        self.task_type = user_dataset['task_type']
        self.size = len(self.dataset)
        self.sentences, self.entities = self.parse()

    def parse(self):
        
        sentences = list()
        entities = list()

        for sample in self.dataset:
            
            tokens = sample['sentence'].split()
            idx2tag = {}
            for label in sample['value']:
                indices = range(label['start'], label['end'])
                idx2tag.update({i:label['tag'] for i in indices})

            labels = list()
            for i, token in enumerate(tokens):
                if idx2tag.get(i) == None:
                    labels.append("O")
                    continue

                labels.append(idx2tag.get(i))

            assert len(labels) == len(tokens), "Unequal token and label sets"

            sentences.append(tokens)
            entities.append(labels)


        return sentences, entities

    def get_dataset(self, size=None):

        return self.sentences[:size], self.entities[:size]

    def show_dataset(self, size=1):

        for i, (tokens, labels) in enumerate(zip(self.sentences, self.entities)):        

            if i>=size:
                break
            
            log(f"Sample {i}:", "green")
            for tk, lb in zip(tokens, labels):
                print(f"{tk}\t{lb}")
            
            print()

    def info(self):
        log(f"Task name: {self.task_name}", "blue")
        log(f"Task ID: {self.task_id}", "green")        
        log(f"Task type: {self.task_type}", "green")
        log(f"Task size: {self.size}\n", "green")        