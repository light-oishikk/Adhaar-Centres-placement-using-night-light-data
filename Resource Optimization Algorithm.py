#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def resource_optimization_algorithm(placement_results, available_resources):
    """
    Resource Optimization Algorithm

    Parameters:
    - placement_results: DataFrame with selected areas for Aadhar center placement
    - available_resources: Dictionary with available resources for each area

    Returns:
    - optimized_resources: DataFrame with optimized resource allocation for Aadhar centers
    """
    # Assuming available_resources is a dictionary with area IDs as keys and available resources as values
    # Example: available_resources = {'area_id_1': 100, 'area_id_2': 150, ...}

    # Sort placement results based on a relevant metric (e.g., population density, demand, etc.)
    sorted_results = placement_results.sort_values(by=['relevant_metric'], ascending=False)

    # Initialize an empty DataFrame for optimized resource allocation
    optimized_resources = pd.DataFrame(columns=['area_id', 'allocated_resources'])

    # Iterate through sorted results and allocate resources based on priority
    for index, row in sorted_results.iterrows():
        area_id = row['gid']
        demand = row['relevant_metric']  # Replace 'relevant_metric' with the actual metric you are optimizing for

        # Check if there are available resources for the area
        if area_id in available_resources:
            allocated_resources = min(demand, available_resources[area_id])
            available_resources[area_id] -= allocated_resources

            # Append the allocation to the optimized_resources DataFrame
            optimized_resources = optimized_resources.append({'area_id': area_id, 'allocated_resources': allocated_resources}, ignore_index=True)

    return optimized_resources

# Example Usage:
available_resources = pd.read_csv('your_available_resources.csv', index_col='area_id')['available_resources'].to_dict()

# Run the resource optimization algorithm
optimized_resources = resource_optimization_algorithm(placement_results, available_resources)

# Print the optimized resource allocation
print("Optimized Resource Allocation:")
print(optimized_resources)



