import streamlit as st

# Function to create a single project display in the grid
def project_card(title, gif_link, page_link):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(gif_link)
    with col2:
        st.markdown(f"### {title}")
        st.markdown(f"[More Info]({page_link})")

# Sidebar with personal information
st.sidebar.header('Your Name')
st.sidebar.write('Your Education Details Here')
# You can add more personal information or links here

# Main page title
st.title('My Projects')

# Sample project data (title, gif link, and page link)
projects = [
    ("Project 1", "path_or_link_to_gif1", "/project1"),
    ("Project 2", "path_or_link_to_gif2", "/project2"),
    # Add more projects as needed
]

# Creating a 6x6 grid for projects
for i in range(0, len(projects), 6):
    cols = st.columns(6)
    for col, project in zip(cols, projects[i:i+6]):
        with col:
            project_card(*project)

# Placeholder for project pages
# You can expand this section with conditional statements to render specific project pages
if 'project1' in st.experimental_get_query_params():
    st.header("Project 1 Details")
    # Add content for Project 1
elif 'project2' in st.experimental_get_query_params():
    st.header("Project 2 Details")
    # Add content for Project 2
# Add more conditions for other projects
