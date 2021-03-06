# Automation and Analysis of Bulk RNA-Sequencing Pipeline 

As a recipient of the Karen T. Romer Undergraduate Teaching and Research Award, I had the opportunity to spend the last 10 weeks collaborating on a research project focusing on analyzing and automating a bulk RNA-sequencing pipeline for [my laboratory](https://ocglab.org/). The published abstract and poster with my findings can be found on the Brown Digital Repository [here](https://repository.library.brown.edu/studio/item/bdr:1139275/). 

# Table of contents

- [Project Introduction](#Automation-and-Analysis-of-Bulk-RNA-Sequencing-Pipeline)
- [Set-up](#Set-up)
- [Usage](#Batch-Script-Usage)
- [Pipeline and Web-app Assessment](#Pipeline-and-Web-app-Assessment)
- [Contribute](#Contributions-and-Future-Directions)
- [License](#license)
- [Footer](#footer)

# Set-up
[(Back to top)](#table-of-contents)

The automation of the bulk RNA-sequencing pipeline relies on a series of batch scripts, which can be found in this repository. These batch scripts are meant to operate under Oscar, Brown University's supercomputer, as well as the Slurm Workload Manager. For a comprehensive guide on how to use these scripts, please email ocglab@brown.edu.  

The Python script to compare differentially expressed genes (DEGs) from any source or model organism to the lab's list of 450 Drosophila candidate synaptic genes can be found in this repository. This web-app runs on Streamlit; click [here](https://docs.streamlit.io/en/stable/) to learn more about Streamlit. 

# Batch Script Usage
[(Back to top)](#table-of-contents)

The batch scripts are meant to be easily adaptable, with various parameters that can be changed at each step of the pipeline. It is important to note that the batch scripts are completed through the expression estimation step. The last step (differential expression) involves an easily-adaptable R script that can be found [here](https://rnabio.org/module-03-expression/0003/03/01/Differential_Expression/) from the Griffith Lab at Washington University.  

# Pipeline and Web-app Assessment
[(Back to top)](#table-of-contents)  

To assess the quality of my pipeline, I compared my differential gene expression results in two CRISPR knockout strains (CRISPR8500 and CRISPR42261) vs. a wild-type strain (w1118) to those reported by Genewiz. The comparative analysis of log2 fold changes, as well as data cleaning can be found in a jupyter notebook under the "Pipeline Analysis" section of this repository. The log2 fold change values for CRISPR8500 vs. w1118 and CRISPR42261 vs. w1118 (ran through my pipeline) can also be found there.

To assess the function of my web-app, ~100 DEGs from an experiment profiling Drosophila genes regulated by high potassium to our candidates resulted in an accurate result of 23 genes in common with the lab's list of synaptic genes.

# Contributions and Future Directions
[(Back to top)](#table-of-contents)

Abstracting the pipeline further to allow for the bash scripts to operate in any cloud computing environment would be ideal. This way, laboratories outside of Brown University would be able to rapidly analyze the results of their own RNA-sequencing experiments. The batch scripts could also be further simplified by merging steps together (i.e. combining the alignment and alignment QC steps).  

More functions can be added to the Python script for the Streamlit web-app. One useful function would be the ability to make comparisons across all species (determine orthologous genes), as the app currently supports FlyBase IDs and FlyBase gene names.

# License
[(Back to top)](#table-of-contents)

[MIT License](https://opensource.org/licenses/MIT)

