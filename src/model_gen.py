import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch

# Load job codes data
job_codes_df = pd.read_csv('jobcodes.csv')  # Update to correct path
descriptions = job_codes_df['description'].tolist()
codes = job_codes_df['code'].tolist()

# Load pre-trained Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L12-v1')  # Efficient and accurate for similarity tasks

# Compute embeddings for each job code description
descriptions_embeddings = model.encode(descriptions, convert_to_tensor=True)

# Save the embeddings for fast future lookups
torch.save(descriptions_embeddings, 'descriptions_embeddings.pt')
torch.save(codes, 'job_codes_list.pt')
