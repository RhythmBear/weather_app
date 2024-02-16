# Weather_app.
A submission for my Python Developer Internship by Adepoju Emmanuel

## Follow the instruction to run the App.

### Technologies Required

In order to run this app make sure you have the following technologies installed on your local machine

- Python
- Git

Once you have installed them you can then proceed with the rest instructions.

Visit this Link and then create an account in order to get access to the API key that we would use to run the App.

[Weather API](https://openweathermap.org/api)


You can clone this repository to your local machine using

```bash
git clone https://github.com/RhythmBear/weather_app.
```
Once you’ve gotten the API key. 
- Create a .env file in you working directory and add the API key like this

```bash
WEATHER_API_KEY = <Your API key>
```

- First Create a Virtual Environment using the following commands.
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    

- Once the Virtual Env has been created. You can install all the requirements needed
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
- Final Step. Run the App and Input the city you want to check the weather for.
    
    ```bash
    python3 run.py
    ```
