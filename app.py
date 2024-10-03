import streamlit as st
import pandas as pd

# Define global variables for column mappings
COLUMN_MAPPINGS = {
    "email_1": "Email",
    "phone_1": "Primary Phone",
    "phone_2": "Mobile Phone",
    "address": "Address",
    "city": "City",
    "state": "State",
    "zip_code": "Zip",
    "insight": "Notes"
}


def main():
    st.title('Real Intent to Propertybase GO Converter')

    st.info("""
    Upload a CSV file. The app will convert your Real Intent CSV into a format that can be imported into Propertybase GO.
    """)

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Check if required columns are in the dataframe
        missing_columns = [col for col in COLUMN_MAPPINGS.keys() if col not in df.columns]

        if 'first_name' not in df.columns:
            missing_columns.append('first_name')
        if 'last_name' not in df.columns:
            missing_columns.append('last_name')

        if not missing_columns:
            df['Name'] = df['first_name'] + " " + df['last_name']
            df = df[['Name'] + list(COLUMN_MAPPINGS.keys())].rename(columns=COLUMN_MAPPINGS)


            # Display the resulting dataframe
            st.write("Converted DataFrame:")
            st.write(df)

            # Download the converted dataframe as CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download converted CSV",
                data=csv,
                file_name='converted_file.csv',
                mime='text/csv',
            )
        else:
            st.write(f"The uploaded file does not contain the required columns: {', '.join(missing_columns)}.")


if __name__ == "__main__":
    main()