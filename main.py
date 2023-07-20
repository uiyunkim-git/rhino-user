import numpy
import pandas as pd



if __name__ == '__main__':
    
    # Sample data for the DataFrame
    data = {
        'Column A': [1, 2, 3, 4, 5],
        'Column B': ['A', 'B', 'C', 'D', 'E'],
        'Column C': [10.1, 20.2, 30.3, 40.4, 50.5]
    }

    # Creating the DataFrame
    df = pd.DataFrame(data)

    # Display the DataFrame
    print(df)

    # Save DataFrame to CSV file
    csv_file_path = '/output/cohort_data.csv'
    df.to_csv(csv_file_path, index=False)

    with open("/output/weight.pt","wb") as f:
        f.write(numpy.array([1,2,3,4,5]).tobytes())
    
    
    print("DataFrame saved to CSV file:", csv_file_path)