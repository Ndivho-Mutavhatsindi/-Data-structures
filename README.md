# ITDPA Project – Patient Scheduling & Social Media Connections Manager  

This repository contains my **second-year ITDPA module project**, which demonstrates the use of **data structures** and **graph algorithms** in solving real-world problems.  

The project is divided into two parts:  

1. **Patient Scheduling System** (Priority Queue)  
2. **Social Media Connections Manager** (Graph/NetworkX)  

---

##  Part 1: Patient Scheduling System  

This component simulates a **hospital patient management system** using a **priority queue**.  
Patients are treated based on urgency (priority value), ensuring critical cases are handled first.  

###  Features
- Add patients with details (Name, Surname, ID, Priority).  
- Retrieve the next patient based on priority.  
- Print the waiting list.  
- Save patient records to a file.  
- Load patient records from a file.  
- Menu-driven console interface.  

###  Implementation
- **Language:** Python  
- **Core Data Structure:** `heapq` (Priority Queue)  

---

##  Part 2: Social Media Connections Manager  

This component models a **mini social network** using **graph data structures**.  
It allows adding users, creating connections, and visualizing the network.  

###  Features
- Add users (nodes) to the network.  
- Create connections (edges) between users.  
- View all users and connections.  
- Display a **graph visualization** of the network using Matplotlib.  

### Implementation
- **Language:** Python  
- **Libraries:**  
  - `networkx` → graph management  
  - `matplotlib` → graph visualization  

---

##  Project Structure
ITDPA_Project/
│── patient_scheduler.py # Patient management system
│── social_network_manager.py # Social media connections manager
│── README.md # Project documentation
│── requirements.txt # Dependencies (for Part 2)
│── .gitignore # Ignore unnecessary files



---

## Running the Project  

### 1. Clone the repository  
```bash
git clone https://github.com/<Ndivho-Mutavhatsindi>/ITDPA_Project.git
cd ITDPA_Project

