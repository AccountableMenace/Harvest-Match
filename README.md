### SPACEnjoyers teams' project for NASA's Space Apps Challenge on data-driven crop yield optimization using soil moisture index assimilation and AI modelling.


# UI
[UI design can be found here](https://www.figma.com/design/ELy0aXk0jRakvz2WMYgf47/HarvestMatch)

# Presentation
[Presentation slides are provided here](https://docs.google.com/presentation/d/e/2PACX-1vTN1PYlGEVe1r41ZWvmqVaFjT6IWO2ALgDgXjSfc-E8aj8wipr1Rgdvpli2vTHaqq1UQvtHgxs7dxV8/pub)


# High-Level Summary

Our project aims to make soil moisture data accessible and easy to understand for new farmers. Recognizing the lack of readily available Earth Observation data, we developed an intuitive app for smartphone and desktop users. Farmers can select an area to receive insights on the best crops to plant, associated costs, and expected profits. We utilize five years of data from NASA's SMAP and ESA's Sentinel-2 satellites in order to provide accurate estimation for the best monetary yielding crop based on the given farm plot. The app combines satellite data to create a historical soil moisture profile and employs a machine learning model to predict soil moisture and optimal crop yields for the upcoming year. Our Best Monetary Yielding Selection Algorithm ranks crops based on profitability while considering soil moisture and regional market data. Additionally, users can upload lab results for precise soil analysis, allowing for tailored recommendations based on specific soil profiles. Ultimately, our project provides actionable insights that help farmers make informed crop decisions, particularly beneficial for beginners. It promotes sustainable practices by aligning crop suggestions with natural moisture levels and is designed for simplicity, making it accessible to users of all technical backgrounds. By harnessing satellite data and AI, we empower farmers to maximize profitability while encouraging efficient resource use.

# Project Details
Our project aims to predict the best monetary yielding crop for an area by analyzing soil moisture levels and other important factors. To be able to do this, we collect data from NASA's SMAP (Soil Moisture Active Passive) satellite and ESA's Sentinel-2 satellite spanning five years. We pay particular attention to Bands 8 (near-infrared) and 12 (shortwave infrared), which are utilized to compute the Soil Moisture Index (SMI). Based on the soil and water requirements of the crops, this information aids in selecting appropriate crops.

The system works through the following process:

**Data Assimilation:** SMAP and Sentinel-2 data from the past five years are collected, and a downscaling technique is applied to increase the spatial resolution to meet the specific dataset requirements.

**Soil Moisture Dataset Creation:** The downscaled data is processed and averaged, creating a comprehensive dataset that represents soil moisture conditions over the last five years.

**Soil Moisture Data Averaging:** The soil moisture data is aggregated and averaged across time periods, smoothing out short-term fluctuations to better reflect long-term trends.

**Soil Moisture Data Prediction for the Upcoming Year:** Based on historical data and trends, a model is used to predict soil moisture conditions for the next year, enabling better crop planning.

**Best Monetary Yielding Crop Selection Algorithm:** This algorithm analyzes soil moisture predictions, historical crop yields, and market prices to identify the crop that will provide the highest economic return.

**List of the Best Yielding Crops:** The algorithm generates a ranked list of crops, prioritizing those expected to deliver the best monetary yields under the forecasted soil moisture conditions.

**Prediction and Algorithms:**

- The first algorithm uses averaged soil moisture dataset along with regional crop cost data and water needs for specific crops to predict the best crops for the upcoming year. It ranks crops from highest to lowest monetary yield based on soil moisture, crop profitability, and water requirements.
- The second algorithm is triggered if the user provides specific lab test results of their soil (including mineral and nutrient levels). This algorithm refines the recommendations by analyzing the compatibility of the soil's mineral composition with the nutrient needs of the crops, offering a more tailored list of crops that would yield the best results based on local soil conditions.

**End-User Interaction:** The system outputs a list of recommended crops ranked by monetary yield. The user can also see additional information regarding the water and nutrient needs of each crop. If users provide their own field-specific lab results, the system adjusts its recommendations to account for specific soil characteristics.

**What it Achieves:** This app empowers farmers, especially those who may lack advanced agronomical knowledge, to maximize their farm's profitability by selecting the best crop for their soil conditions. It offers flexibility by allowing farmers to use general regional data or more precise, field-specific data to get tailored crop recommendations.

**Tools and Technologies:**

- **Programming:** Python is used to process satellite data, train the AI model, and develop the selection algorithms.
- **Satellite Data:** NASA's SMAP data and ESA's Sentinel-2 data are used for soil moisture monitoring, while local agricultural databases provide crop cost and water requirement data.
- **Server Infrastructure:** Robust servers are necessary for data gathering, AI model training, and processing. The system is designed to become more efficient with increased usage, reducing the computational cost per field over time.



**Created by:**
- Laurynas Arštikys
- Justas Fedorovičius
- Kasparas Mičiūnas
- Dominykas Petrulaitis
