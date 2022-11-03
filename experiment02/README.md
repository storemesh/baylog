# Experiment02
This experiment is used Local Outlier Factor, Isolation Forest and Elliptic Envelope to detect abnormaly behavior from keyword in logs files. The dataset were generated from Django server and Nginx with specific behavior.

## Run Step
1. (Optional) Generate Logs     
    The step 1.1 - 1.3 are to generate new logs data. If you want to use the original logs data that were used in the paper. Download files in this [link](https://drive.google.com/drive/u/1/folders/1xQiKw7zyx631wHvuxHRfsuO1yG1DiRP5) and put it in `/experiment02/input` instead   
  
    - 1.1 Start Django server and Nginx with docker compose 
        ```sh
        cd experiment02/django
        docker compose up
        ```

    - 1.2 Open new terminal, activate python environment and start jupyter notebook
        ```sh
        conda activate baylog-experiment
        jupyter notebook
        ```
    - 1.3 Generate new user in Django server by running all cell in `experiment02/01_generate_user.ipynb`
    - 1.4 Generate Normal behavior logs 
        - 1.4.1 running locust
            ```sh
            cd locust
            locust
            ```
        - 1.4.2 open `http://localhost:8089/` and type the following in popup
            - Number of users: 50
            - Spawn Rate: 1
            - Host: http://localhost/api/v1
        - 1.4.3 wait around 2 minutes and stop generate request
    - 1.5 Generate scan, error and timeout logs by running all cell in `experiment02/02_generate_scan-error-timeout_log.ipynb`   

    **Note:** you can choose your desired time to start generate logs, but need to change start time in preprocess step in 2.1.1 and 2.2.1 of `experiment02/03_generate_result.ipynb`.


2. train model and save result by running all cell in `experiment01/03_generate_result.ipynb`  
    **Note:** The result will not be exactly the same value in the paper, but it should be similar
