from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2, ECS, EKS, Lambda
from diagrams.aws.database import RDS, Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.network import ELB, VPC
from diagrams.aws.storage import S3


def notebook_step_001() -> None:
    "Generated from Jupyter notebook: aws_architecture_diagrams\n\nMagics and shell lines are commented out. Run with a normal Python interpreter."


def notebook_step_003() -> None:
    with Diagram("Grouped Workers", show=True, direction="TB"):
        (
            ELB("lb")
            >> [
                EC2("worker1"),
                EC2("worker2"),
                EC2("worker3"),
                EC2("worker4"),
                EC2("worker5"),
            ]
            >> RDS("events")
        )


def diagram_py() -> None:
    with Diagram("Web Service", show=True):
        ELB("lb") >> EC2("web") >> RDS("userdb")


def notebook_step_006() -> None:
    with Diagram("Event Processing", show=True):
        source = EKS("k8s source")
        with Cluster("Event Flows"):
            with Cluster("Event Workers"):
                workers = [ECS("worker1"), ECS("worker2"), ECS("worker3")]
            queue = SQS("event queue")
            with Cluster("Processing"):
                handlers = [Lambda("proc1"), Lambda("proc2"), Lambda("proc3")]
        store = S3("events store")
        dw = Redshift("analytics")
        vpc = VPC("VPC")
        source >> workers >> queue >> handlers
        handlers >> store
        handlers >> dw >> vpc


def notebook_step_007() -> None:
    with Diagram("Event Processing", show=True):
        source = EKS("k8s source")
        with Cluster("Event Flows"):
            with Cluster("VPC"):
                workers = [ECS("worker1"), ECS("worker2"), ECS("worker3")]
            queue = SQS("event queue")
            with Cluster("Processing"):
                handlers = [Lambda("proc1"), Lambda("proc2"), Lambda("proc3")]
        store = S3("events store")
        dw = Redshift("analytics")
        source >> workers >> queue >> handlers
        handlers >> store
        handlers >> dw


def notebook_step_008() -> None:
    with Diagram("Grouped Workers", show=True):
        ELB("lb") >> [EC2("worker1")] >> RDS("events") >> RDS("events")
        (
            ELB("lb")
            >> [EC2("worker2"), EC2("worker3"), EC2("worker4"), EC2("worker5")]
            >> RDS("events")
        )


def download_an_image_to_be_used_into_a_custom_node() -> None:
    """Work-order diagram with custom icons (requires image assets in cwd)."""
    from diagrams.custom import Custom

    user = "User_light-bg@4x.png"
    sap_logo = "2000px-SAP-Logo.png"
    users = "Users_light-bg@4x.png"
    primavera = "primavera.png"
    e2open_logo = "e2open.png"
    iris_logo = "IRIS.png"
    with Diagram("Work Order Process", show=True):
        sap_process = Custom("SAP", sap_logo)
        e2open = Custom("E2Open", e2open_logo)
        iris = Custom("IRIS", iris_logo)
        Custom("Operator identifies an issue", user)
        Custom("Risk Based Work Selection", users)
        Custom("Primavera P6", primavera)
        sap_process >> e2open >> iris


def download_an_image_to_be_used_into_a_custom_node_2() -> None:
    """Extended work-order diagram with AWS analytics path."""
    from diagrams.custom import Custom

    user = "User_light-bg@4x.png"
    sap_logo = "2000px-SAP-Logo.png"
    primavera = "primavera.png"
    e2open_logo = "e2open.png"
    iris_logo = "IRIS.png"
    sagemaker_logo = "Amazon-SageMaker_light-bg@4x.png"
    quicksight_logo = "Amazon-Quicksight@4x.png"
    with Diagram("Work Order Process", show=True):
        with Cluster("AWS"):
            Custom("SAP C-FIN \n (HANA S/4)", sap_logo) >> Custom(
                "SageMaker", sagemaker_logo
            )
            Custom("SageMaker", sagemaker_logo) >> Custom("Quicksight", quicksight_logo)
        operator = Custom("Operator identifies an issue", user)
        sap_process = Custom("SAP", sap_logo)
        schedule = Custom("Primavera P6", primavera)
        e2open = Custom("E2Open", e2open_logo)
        iris = Custom("IRIS", iris_logo)
        operator >> sap_process >> schedule >> e2open
        sap_process >> e2open >> iris


def event_processing_with_vpc_cluster() -> None:
    with Diagram("Event Processing", show=True):
        source = EKS("k8s source")
        with Cluster("Event Flows"):
            with Cluster("VPC"):
                workers = [ECS("worker1"), ECS("worker2"), ECS("worker3")]
            queue = SQS("event queue")
            with Cluster("Processing"):
                handlers = [Lambda("proc1"), Lambda("proc2"), Lambda("proc3")]
        store = S3("events store")
        dw = Redshift("analytics")
        source >> workers >> queue >> handlers
        handlers >> store
        handlers >> dw


def main() -> None:
    notebook_step_001()
    notebook_step_003()
    diagram_py()
    notebook_step_006()
    notebook_step_007()
    notebook_step_008()
    download_an_image_to_be_used_into_a_custom_node()
    download_an_image_to_be_used_into_a_custom_node_2()
    event_processing_with_vpc_cluster()


if __name__ == "__main__":
    main()
