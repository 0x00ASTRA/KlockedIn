"""
Author: ASTRAEUS
Date: 2024-11-9

 This file is part of KlockedIn.
  KlockedIn is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.
  KlockedIn is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  You should have received a copy of the GNU General Public License
  along with KlockedIn.  If not, see <https://www.gnu.org/licenses/>.
"""

from sentence_transformers import SentenceTransformer, util
import torch
import pandas as pd

# Load precomputed embeddings and model
model = SentenceTransformer('msmarco-distilbert-dot-v5')
descriptions_embeddings = torch.load('descriptions_embeddings.pt', weights_only=True)
job_codes = torch.load('job_codes_list.pt', weights_only=True)
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

def find_best_job_codes(description):
    # Encode the input description
    input_embedding = model.encode(description, convert_to_tensor=True)
    # Compute cosine similarity with all job code descriptions
    similarities = util.cos_sim(input_embedding, descriptions_embeddings)
    best_matches = torch.topk(similarities, k=5)
    best_match_codes = [job_codes[idx] for idx in best_matches.indices[0]]
    best_match_descriptions = [descriptions[idx] for idx in best_matches.indices[0]]
    confidences = [similarities[0, idx].item() * 100 for idx in best_matches.indices[0]]  # Convert to percentage

    return best_match_codes, confidences, best_match_descriptions

# Example usage
run = True
exit_phrases = ["exit", "quit", "stop", "bye"]
while(run):
    description = input("Describe what you did today: ")
    if description.lower() in exit_phrases:
        run = False
        print("Session terminated.")
        print("\nGoodbye!")
        break
    # best_code, confidence, best_match_description = find_best_job_code(description)
    # print(f"Best Matching Job Code: {best_code}, Job Description: {best_match_description}, Confidence: {confidence}%")
    best_codes, confidences, best_match_descriptions = find_best_job_codes(description)
    print("=== Best Matching Job Codes: ===")
    for code, confidence, description in zip(best_codes, confidences, best_match_descriptions):
        print(f"Job Code: {code}, Job Description: {description}, Confidence: {confidence}%")
    print("================================\n")