# Framework setup

### Set env variables
##### Create `.env` file based on `env.example` file

## Installation
##### Install Python
```
Version 3.9 or higher
```
##### Clone project
```
git clone https://github.com/romanbarabash/pytest_wix.git
```
##### Creating a virtual environment
```
python -m venv venv
```
##### Activating a virtual environment  
Linux or macOS:
```
source venv/bin/activate
```
Windows:
```
.\venv\Scripts\activate
```
##### Installing packages
```
pip install -r requirements.txt
```

##### Run all tests locally under root and generate allure report: 

```
pytest tests  --alluredir ./allure-results
```
##### Run Allure server locally:
```
allure generate allure-results --clean  
```
##### Allure should open report the under new tab




