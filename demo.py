import streamlit as st
import matplotlib.pyplot as plt

def get_filenames_lengths(files):
    lengths = [len(file.name) for file in files]
    return lengths

def draw_length_distribution_histogram(lengths):
    st.write("## Filename Length Distribution")
    st.write("Histogram showing the distribution of filename lengths.")
    fig, ax = plt.subplots()
    ax.hist(lengths, bins=20)
    st.pyplot(fig)

def main():
    st.title("PDF Files Downloader with Filename Length Distribution")
    
    st.write("### Upload PDF Files")
    uploaded_files = st.file_uploader("Upload PDF files here", type=['pdf'], accept_multiple_files=True)

    if uploaded_files:
        lengths = get_filenames_lengths(uploaded_files)
        
        st.success("Files successfully processed!")
        
        draw_length_distribution_histogram(lengths)

if __name__ == "__main__":
    main()