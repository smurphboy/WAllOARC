[![Netlify Status](https://api.netlify.com/api/v1/badges/ee42e5f7-6f9d-49e0-9cdb-c27a76197ca2/deploy-status)](https://app.netlify.com/sites/silver-alfajores-965b56/deploys)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/smurphboy/WAllOARC/WorkedAllOARC.ipynb)

# Worked All OARC

## tl;dr

A fun contest aiming to bring members of OARC together through radio.

## What does this notebook do?

1. Reads the QSO submissions from the Google Form via a Google Sheet
2. Imports into a pandas dataframe
3. Cleans the callsign and validates it is a valid DXCC (and spits out rows to check for errors)
4. Plots some basic statistics / graphs and Leaderboards
