# Practical Work: Itemsets and Association Rules Mining
Class project under the supervision of Yannick Toussaint for the Data Mining class.

Realized by Maxime Guillaume and Esteban Marquer.

## Outline
## Installation and Dependencies
This project was realized using SPMF v2.39.

To run the utility scripts you will need Python 3.7 with the following libraries:
- `click` (version 7 or more recent): a command line interface (CLI) library;
- `pandas` (version 0.25 or more recent): a data handling library;
- `sklearn` (version 0.21 or more recent): a machine learning and data processing library;
- `pickle` (should be provided with Python 3.7): an object serialization library.

To run the Bash scripts (`.sh` files) used in the project, use linux system or any Bash interpreter accepting the following Bash commands:
- `python`;
- `wc`;
- `mkdir`;
- `sort`;
- `uniq`;
- `echo`.

## Usage
## Files
### Output Folders for Itemset Extraction
- [`Patterns`](./Patterns): folder containing the encoded patterns (frequent itemsets) extracted using the FPClosed and the FPGrown algorithms with different values for the `min_sup`. Those files corresponds to the raw outputs of SPMF. Each file name correspond to `<algorithm>_<min support (in %)>.txt`.
- [`DecodedPatterns`](./DecodedPatterns): folder containing the decoded patterns (frequent itemsets) extracted using the FPGrown algorithm with different values for the `min_sup`. Each file name correspond to `<algorithm>_<min support (in %)>.txt`.
- [`DecodedPatterns/Diff`](./DecodedPatterns/Diff): folder containing the patterns (frequent itemsets) extracted using the FPGrown algorithm, groupped by slices of support. Each file name correspond to `<algorithm>_<min support (in %)>_<max support (in %)>.txt`.

### Output Folders for Association Rule Extraction
- [`Rules`](./Rules): folder containing the encoded association rules extracted using the FPGrown algorithm with different values for the `min_sup` and the `min_conf`. Those files corresponds to the raw outputs of SPMF. Each file name correspond to `<algorithm>_<min support (in %)>_<min confidence (in %)>.txt`.
- [`DecodedRules`](./DecodedRules): folder containing the decoded association rules extracted using the FPGrown algorithm with different values for the `min_sup` and the `min_conf`. Each file name correspond to `<algorithm>_<min support (in %)>_<min confidence (in %)>.txt`.
- [`FilteredRules`](./FilteredRules): folder containing a subset of the decoded association rules extracted using the FPGrown algorithm, with only rules deemed "interesting" for our analysis (see more in the report). Each file name correspond to `<algorithm>_<min support (in %)>_<min confidence (in %)>.txt`.

### Sources and Scripts ([`Src`](./Src) folder)
The recommended use of the scripts is to use the launching Bash scripts from the root of the repository.

- [`Src/filter_rules.py`](./Src/filter_rules.py): Python script to filter the rules deemed "interesting" for our analysis (see more in the report) in a single file. Run `python Src/filter_rules.py --help` for more information.
- [`Src/spmf_encoding.py`](./Src/spmf_encoding.py): Python scripts to encode and decode data (see more in the report). Run `python Src/spmf_encoding.py --help` for more information.


- [`Src/count_item.sh`](./Src/count_item.sh): pure Bash script to enumerate the number of itemsets in the [`Patterns`](./Patterns) folder.
- [`Src/count_rules.sh`](./Src/count_rules.sh): pure Bash script to enumerate the number of association rules in the [`Rules`](./Rules) folder.

- [`Src/decode_itemsets.sh`](./Src/decode_itemsets.sh): launching script for the decoding tool in [`Src/spmf_encoding.py`](./Src/filter_rules.py), applying it on every file in [`Patterns`](./Patterns) and outputing in [`DecodedPatterns`](./DecodedPatterns).
- [`Src/decode_rules.sh`](./Src/decode_rules.sh): launching script for the decoding tool in [`Src/spmf_encoding.py`](./Src/filter_rules.py), applying it on every file in [`Rules`](./Rules) and outputing in [`DecodedRules`](./DecodedRules).

- [`Src/diff.sh`](./Src/diff.sh): pure Bash script to group the itemsets in the [`DecodedPatterns`](./DecodedPatterns) folder by slices of support and outputing in [`DecodedPatterns/Diff`](./DecodedPatterns/Diff).

- [`Src/filter_rules.sh`](./Src/filter_rules.sh): launching script for the [`Src/filter_rules.py`](./Src/filter_rules.py) script on every file in [`DecodedRules/`](./DecodedRules).

- [`Src/encode.sh`](./Src/encode.sh): launching script for the encoding tool in [`Src/spmf_encoding.py`](./Src/filter_rules.py), applying it on every file in [`GrandEst`](./GrandEst) and outputing the `binary_grand_est.csv` file (currently archived in [`binary_grand_est.csv.zip`](./binary_grand_est.csv.zip)).

### Other Files

- `GrandEst` (not present in the repository): CSV file of the corpus, with `;` separator.

- [`binary_grand_est.csv.zip`](./binary_grand_est.csv.zip): archive containing the encoded, binarized and column-filtered corpus.

- [`columns.txt`](./columns.txt): file containing all the column names of the columns to keep during the preprocessing.
- [`housing.txt`](./housing.txt): file containing the subset of the column names in [`columns.txt`](./columns.txt) corresponding to the housing.
- [`person.txt`](./person.txt): file containing the subset of the column names in [`columns.txt`](./columns.txt) corresponding to the socio-economic situation.

- [`le.pickle`](./le.pickle): pickled label encoder from `sklearn`, created by the encoding script and used to decode the outputs from SPMF.

- [`Report.pdf`](./Report.pdf): a report describing the implementation choices and answering the questions from the instruction sheet.
- [`SignificationDesVariables.pdf`](./SignificationDesVariables.pdf): (in French) PDF file describing the various fields in the data.