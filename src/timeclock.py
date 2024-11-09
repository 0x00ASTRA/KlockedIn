from sentence_transformers import SentenceTransformer, util
import torch
import pandas as pd

# Load precomputed embeddings and model
model = SentenceTransformer('all-MiniLM-L12-v1')
descriptions_embeddings = torch.load('descriptions_embeddings.pt')
job_codes = torch.load('job_codes_list.pt')
job_codes_df = pd.read_csv('jobcodes.csv')
descriptions = job_codes_df['description'].tolist()

def find_best_job_code(description):
    # Encode the input description
    input_embedding = model.encode(description, convert_to_tensor=True)

    # Compute cosine similarity with all job code descriptions
    similarities = util.cos_sim(input_embedding, descriptions_embeddings)
    best_match_idx = torch.argmax(similarities).item()
    best_match_code = job_codes[best_match_idx]
    best_match_description = descriptions[best_match_idx]
    confidence = similarities[0, best_match_idx].item() * 100  # Convert to percentage

    return best_match_code, confidence, best_match_description

# Example usage
description = "Installed acoustic tiling in the main office"
best_code, confidence, best_match_description = find_best_job_code(description)
print(f"Best Matching Job Code: {best_code}, Job Description: {best_match_description}, Confidence: {confidence}%")
