# Experiment01
This experiment is used Local Outlier Factor, Isolation Forest and Elliptic Envelope to detect abnormaly behavior from number of requests in timeseries dataset. The dataset were generated from specific distribution. 

## Run Step
1. Activate Python Environment
    ```sh
    conda activate baylog-experiment
    ```
2. Start jupyter notebook
    ```sh
    jupyter notebook
    ```
3. (optional) Generate dataset by running all cell in `experiment01/01_generate_abnormal_dataset.ipynb`   

    **Note:** This step are to generate new dataset. If you want to use the original dataset that were used in the paper. Download files in this [link](https://drive.google.com/drive/u/1/folders/1CmcH0z2klFDXQxin8pY0w2PsZXxT1z07) and put it in `/experiment01/input` instead    

4. Train model and save result by running all cell in `experiment01/02_generate_result.ipynb`

5. Generate ROC Curve and prediction visualization by running all cell in `experiment01/03_print_report.ipynb.ipynb`    

    **Note:** The result will not be exactly the same value in the paper, but it should be similar