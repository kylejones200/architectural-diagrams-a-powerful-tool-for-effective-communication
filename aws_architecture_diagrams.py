"""Generated from Jupyter notebook: aws_architecture_diagrams

Magics and shell lines are commented out. Run with a normal Python interpreter."""


# --- code cell ---

# ! pip install diagrams  # Jupyter-only


# --- code cell ---

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Grouped Workers", show=True, direction="TB"):
    ELB("lb") >> [EC2("worker1"),
                  EC2("worker2"),
                  EC2("worker3"),
                  EC2("worker4"),
                  EC2("worker5")] >> RDS("events")


# --- code cell ---

# ! pip install graphviz  # Jupyter-only


# --- code cell ---

# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service", show=True):
    ELB("lb") >> EC2("web") >> RDS("userdb")


# --- code cell ---

from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift 
from diagrams.aws.integration import SQS 
from diagrams.aws.storage import S3  
with Diagram("Event Processing", show=True):   
    source = EKS("k8s source")      
    with Cluster("Event Flows"):        
        with Cluster("Event Workers"):          
            workers = [ECS("worker1"),   
                       ECS("worker2"),
                       ECS("worker3")]
        queue = SQS("event queue")  
        with Cluster("Processing"):       
            handlers = [Lambda("proc1"),                             
                        Lambda("proc2"),                      
                        Lambda("proc3")]     
    store = S3("events store")    
    dw = Redshift("analytics")
    VPC = VPC('VPC')
 
    source >> workers >> queue >> handlers  
    handlers >> store 
    handlers >> dw >> VPC


# --- code cell ---

from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift 
from diagrams.aws.integration import SQS 
from diagrams.aws.storage import S3  
from diagrams.aws.network import VPC 

with Diagram("Event Processing", show=True):   
    source = EKS("k8s source")      
    with Cluster("Event Flows"):        
        with Cluster("VPC"):          
            workers = [ECS("worker1"),   
                       ECS("worker2"),
                       ECS("worker3")]
        queue = SQS("event queue")  
        with Cluster("Processing"):       
            handlers = [Lambda("proc1"),                             
                        Lambda("proc2"),                      
                        Lambda("proc3")]     
    store = S3("events store")    
    dw = Redshift("analytics")     
 
    source >> workers >> queue >> handlers  
    handlers >> store 
    handlers >> dw


# --- code cell ---

with Diagram("Grouped Workers", show=True):
    ELB("lb") >> [EC2("worker1")] >>RDS("events") >> RDS("events")
    ELB("lb") >> [EC2("worker2"),
                  EC2("worker3"),
                  EC2("worker4"),
                  EC2("worker5")] >> RDS("events")


# --- code cell ---

from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.aws.database import Aurora
from diagrams.k8s.compute import Pod

# Download an image to be used into a Custom Node class
user = "User_light-bg@4x.png"
SAP = "2000px-SAP-Logo.png"
users = "Users_light-bg@4x.png"
primavera = "primavera.png"
e2open = "e2open.png"
iris = "IRIS.png"



with Diagram("Work Order Process", show=True):

    Operator = Custom("Operator identifies an issue", user)
    SAP_process = Custom("SAP", SAP)
    RBWS = Custom("Risk Based Work Selection", users)
    Schedule = Custom("Primavera P6", primavera)
    E2Open = Custom("E2Open", e2open)
    IRIS = Custom("IRIS", iris)
    c_fin = Custom("SAP C-FIN \n (HANA S/4)", SAP)
    sagemaker = Custom("SageMaker", sagemaker)
    quicksight = Custom("Quicksight", quicksight)        
    
    SAP_process >> E2Open >> IRIS


# --- code cell ---

from urllib.request import urlretrieve

from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.aws.database import Aurora
from diagrams.k8s.compute import Pod

# Download an image to be used into a Custom Node class
user = "User_light-bg@4x.png"
SAP = "2000px-SAP-Logo.png"
users = "Users_light-bg@4x.png"
primavera = "primavera.png"
e2open = "e2open.png"
iris = "IRIS.png"
sagemaker = "Amazon-SageMaker_light-bg@4x.png"
quicksight = "Amazon-Quicksight@4x.png"


with Diagram("Work Order Process", show=True):
    AWS - 
    with Cluster("AWS"):          
            Custom("SAP C-FIN \n (HANA S/4)", SAP) >> Custom("SageMaker", sagemaker)
            Custom("SageMaker", sagemaker) >> Custom("Quicksight", quicksight)
            
    Operator = Custom("Operator identifies an issue", user)
    SAP_process = Custom("SAP", SAP)
    #RBWS = Custom("Risk Based Work Selection", users)
    Schedule = Custom("Primavera P6", primavera)
    E2Open = Custom("E2Open", e2open)
    IRIS = Custom("IRIS", iris)
    
    Operator >> AWS >> RBWS >> SAP_process >> Schedule >> E2Open
    SAP_process >> E2Open >> IRIS
    

from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift 
from diagrams.aws.integration import SQS 
from diagrams.aws.storage import S3  
from diagrams.aws.network import VPC 

with Diagram("Event Processing", show=True):   
    source = EKS("k8s source")      
    with Cluster("Event Flows"):        
        with Cluster("VPC"):          
            workers = [ECS("worker1"),   
                       ECS("worker2"),
                       ECS("worker3")]
        queue = SQS("event queue")  
        with Cluster("Processing"):       
            handlers = [Lambda("proc1"),                             
                        Lambda("proc2"),                      
                        Lambda("proc3")]     
    store = S3("events store")    
    dw = Redshift("analytics")     
 
    source >> workers >> queue >> handlers  
    handlers >> store 
    handlers >> dw
