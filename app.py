import streamlit as st

def main():
    st.title("My Streamlit App")
    st.write("Hello, world!")
    
    # Get the URL parameters
    params = st.experimental_get_query_params()
    
    # Define the default values for the parameters
    default_name = "John"
    default_age = 30
    
    # Get the values of the "name" and "age" parameters from the URL
    name = params.get("name", [default_name])[0]
    age = params.get("age", [default_age])[0]
    
    # Display the values of the parameters
    st.write("Name:", name)
    st.write("Age:", age)

if __name__ == "__main__":
    main()