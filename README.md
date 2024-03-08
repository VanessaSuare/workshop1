# workshop1 Candidates
This workshop is a real exercise of a job interview so it will give you a better understanding about a recruitment process

## Proyect Structure

The structure of the directories and files is as follows:

<div style="background-color: #000000;font-size: 14px ;color: #FFFFFF; padding: 10px; border: 1px solid #ccc">
    <pre>
        .
        ├── .gitignore
        ├── README.md
        ├── config
        │   └── config.py
        ├── data
        │   ├── candidates.csv
        │   └── candidates_EDA.csv
        ├── documents
        │   └── document_workshop1.pdf
        ├── notebooks
        │   └── eda_candidates_hired.ipynb
        ├── src
        │   └── main.py
        └── visualization
            ├── workshop_visualization.pdf
            └── workshop_visualization.pbix
    </pre>
</div>

## Installation Requirements

To run the project, these are the libraries you need to have installed

- pandas

- matplotlib

- seaborn

- sqlalchemy

These can be installed using pip like this:

<div style="background-color: #000000;font-size: 14px ;color: #FFFFFF; padding: 10px; border: 1px solid #ccc">
    <pre>
        pip install <library_name>
    </pre>
</div>

## Proyect Execution

1.  Specify the location where you want to host the project, then use this command to clone the repository inside the folder:

<div style="background-color: #000000;font-size: 14px ;color: #FFFFFF; padding: 10px; border: 1px solid #ccc">
    <pre>
        git clone <url_del_repositorio>
    </pre>
</div>

1.1 Enter the project with this command (you must run this inside the folder where you are cloning the repository):

<div style="background-color: #000000;font-size: 14px ;color: #FFFFFF; padding: 10px; border: 1px solid #ccc">
    <pre>
        cd workshop1
    </pre>
</div>

2.  Execute the file "main.py" to load the dataset from the csv file to the PostgreSQL, you can do it with this command:

<div style="background-color: #000000;font-size: 14px ;color: #FFFFFF; padding: 10px; border: 1px solid #ccc">
    <pre>
        python src/main.py
    </pre>
</div>

3.  Open and run the Jupyter notebook "EDA.ipynb".

4.  Finally you can see the visualization of this data in PowerBI, by opening the file WorkshopVisualization.pbix .