# TerrainBasedSwitching
TSP or Terrain Based Switching 

## Introduction
There are 3 types of envs:
1. Cobblestone
2. Gravel
3. Sandpaper

### 1. Cobblestone
#### 1.1. Cobblestone
![Cobblestone](images/cobblestone.png)
#### 1.2. Loose Cobblestone
![Loose Cobblestone v1](images/cobblestone_loose_v1.png)
![Large Loose Cobblestone v2](images/cobblestone_loose_v2.png)

### 2. Gravel
![Gravel](images/gravel.png)

### 3. Sandpaper
![Sandpaper](images/sandpaper.png)

## Relevant Files
```

├── README.md
├── images
├── TSP
│   ├── xml
│   │   ├── cobblestone_hopper.xml
│   │   ├── cobblestone_hopper_loose_v1.xml
│   │   ├── cobblestone_hopper_loose_v2.xml
│   │   ├── sandpaper_hopper.xml
│   │   └── gravel_hopper.xml
│   ├── notebooks
│   │   ├── baseline_online_RL.ipynb
│   │   ├── cobblestone_hopper_loose_v1.ipynb
│   │   ├── standard_hopper.ipynb
│   │   ├── sandpaper_hopper.ipynb
│   │   ├── TSP_oracle.ipynb
│   │   ├── TSP.ipynb
│   │   ├── Evaluation.ipynb
│   │   └── Visualization.ipynb
│   ├── policies
│   │   ├── cobblestone_hopper_loose_v1
│   │   ├── standard_hopper
│   │   ├── sandpaper_hopper
|   |   ├── online_RL_policy
|   |   ├── TSP_oracle
│   │   └── TSP
│   └── data
│       └── data_generation
├── archive (temporary)

```

## How to run

### 1. Open the notebook in colab 

### 2. Run the notebook until 'allowing access to google drive' cell

### 3. Mount google drive, and Create a folder envs/ inside the following directory:
```
 usr/local/lib/python3.7/dist-packages/gym/envs/mujoco/assets
```
### 4. Copy the xml files from TSP/xml/ to the envs/ folder

### 5. Run the rest of the notebook

## Results

Here we include a short video of the TSP agent in action. The agent is trained on the cobblestone environment and is tested on the sandpaper environment. The agent is able to adapt to the new environment and perform well.

![TSP agent in action](images/TSP_agent_in_action.gif)