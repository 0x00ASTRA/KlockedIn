# AI Job Code Helper

I started this project because of the frustrations I used to have trying to find the right job code to fill in on my time card. Accountants would always get pissed off becuase some code wasn't right or the time card wasnt filled out. Thanks to this project, that headache is gone.

## Usage

**Prerequisites:**
- python3.12

**Clone the project:**
`git clone https://github.com/0x00ASTRA/KlockedIn.git && cd KlockedIn`

**Create the virtual enviroment:**
`python3 -m venv venv`

**Activate the enviroment:**
>*Linux/Mac:*
>`source venv/bin/activate`

>*Windows:*
>`./venv/Scripts/Activate.ps1`

**Install requirements:**
`pip3 install -r requirements.txt`

**Run the program:**
`python3 src/timeclock.py`

## Output Example
```
Describe what you did today: cleaned toilets
Best Matching Job Codes:
Job Code: 9014, Job Description: Restrooms-cleaning, Confidence: 93.2257890701294%
Job Code: 9402, Job Description: Sewer cleaning, Confidence: 90.9314215183258%
Job Code: 9402, Job Description: Beach cleaning-, Confidence: 86.75729632377625%
Job Code: 5610, Job Description: Cleaner-debris removal, Confidence: 86.38885021209717%
Job Code: 9402, Job Description: Septic tank cleaning, Confidence: 86.18484139442444%
```

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.