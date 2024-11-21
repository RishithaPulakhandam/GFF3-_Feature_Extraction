**GFF3 Feature Exporter**

#### Description
This script allows users to extract specific features from a GFF3 file and display their corresponding FASTA sequences. It supports queries based on feature type, attribute, and value, producing results in a standard FASTA format.

#### Features
1. Reads and processes GFF3 files containing feature annotations and FASTA sequences.
2. Filters features based on:
   - **Feature Type** (e.g., gene, mRNA).
   - **Attribute** (e.g., ID, Name).
   - **Value** of the specified attribute.
3. Outputs matching feature information and FASTA sequence in 60-character-per-line format.
4. Handles multiple matches by warning the user and showing the first match.
5. Provides user-friendly messages if no matches are found.

#### Usage
The script is executed via the command line with the following format:
  ```bash
   python3 export_gff3_feature.py --source_gff=/path/to/file.gff3 --type=<feature_type> --attribute=<attribute> --value=<value>
  ```
**Example Commands:**
- Extracting a gene with a specific ID:
  ```bash
  python3 export_gff3_feature.py --source_gff=/path/to/file.gff3 --type=gene --attribute=ID --value=YAR003W
  ```
- Querying a feature not present in the file:
  ```bash
  python3 export_gff3_feature.py --source_gff=/path/to/file.gff3 --type=gene --attribute=ID --value=INVALID_ID
  ```

#### Output
- **Header:** Displays the feature type, attribute, and value.
  ```
  >gene:ID:YAR003W
  ```
- **FASTA Sequence:** The corresponding DNA sequence formatted in lines of 60 characters each.

#### Requirements
- Python 3.x
- Input file in valid GFF3 format (must include `##FASTA` section).

#### Testing
- **Positive Test Cases:** Run the script with valid feature types and attributes that exist in the file.
- **Negative Test Cases:** Test with non-existent attributes or values to confirm graceful error handling.
