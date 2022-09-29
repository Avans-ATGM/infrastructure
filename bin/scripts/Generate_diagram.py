from diagrams import Cluster, Diagram
from diagrams.onprem.compute import Server
from diagrams.onprem.database import InfluxDB
from diagrams.onprem.monitoring import Grafana
from diagrams.onprem.logging import Loki
from diagrams.programming.language import Bash
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.vcs import Github
from diagrams.onprem.client import Client
from diagrams.onprem.network import Nginx
from diagrams.onprem.container import Docker
from diagrams.generic.os import Ubuntu
from diagrams.onprem.iac import Ansible

#overview
# globally of what we have
with Diagram("Global overview", show=False):

    with Cluster("Production machines"):
        # Galaxy server
        with Cluster("Dif maintained machines"):
            Cocalc_server = Server("Cocalc")
            galaxy_server = Server("Galaxy")
            galaxy_server_test = Server("Test Galaxy")

        Nginx_galaxy = Nginx("Nginx")
        with Cluster("web servers galaxy"):
            galaxy_web_servers =  [Grafana("monitoring"),
                                   Client("Galaxy"),
                                   Jenkins("Jenkins galaxy & cocalc")]

        #Test Galaxy
        Nginx_galaxy_test = Nginx("Nginx")
        with Cluster("web servers galaxy for testing"):
            galaxy_web_servers_test =  [Client("Galaxy")]

        #Cocalc

        Nginx_Cocalc = Nginx("Nginx")
        docker = Docker("Docker")

        with Cluster("Container"):
           cocalc = [Client("Cocalc")]

    Cocalc_server >> Nginx_Cocalc  >> cocalc
    Cocalc_server >> docker >> cocalc
    galaxy_server >> Nginx_galaxy >> galaxy_web_servers
    galaxy_server_test >> Nginx_galaxy_test >> galaxy_web_servers_test

    with Cluster("Users machines"):
        with Cluster("Local machines"):
            Isengard = Server("Isengard")
            Erebor = Server("Erebor")
            Asgard = Server("Asgard")
            Midgard = Server ("Midgard")

        with Cluster("online machines"):
            surf = Server("Surf Sara archive")
        with Cluster("Jenkins webserver all"):
            Jenkins_isengard = [Jenkins("Jenkins  all")]
        with Cluster("Purpose"):
            Interns = Ubuntu("Interns & Teachers")
            Students = Ubuntu("Student & Teachers")
            General = Ubuntu("General, overload galaxy")
            overload = Ubuntu("General, overload galaxy")

        User_servers =[
            Erebor >>  overload,
            Asgard >>  General,
            Midgard >>  Students,
            Isengard >> Students,
            Isengard >> Nginx("Nginx") >> Jenkins_isengard
        ]

    surf << Erebor
    surf << Asgard
    surf << Midgard
    surf << Isengard


    #Isengard
#Grafana
with Diagram("Monitoring servers with Grafana", show=False):
    with Cluster("User Servers"):
        servers_user = [Server("Midgard"),
                   Server("Asgard"),
                   Server("Isengard"),
                   Server("Erebor")]

    with Cluster("production Servers"):
        servers_prod = [Server("Galaxy"),
                   Server("Galaxy test"),
                   Server("Cocalc")]


    Logging = Loki("Telegraf")

    with Cluster("Grafana infrastructure"):
        Data_storage = InfluxDB("Influx database")
        grafana = Grafana("monitoring")
        server_grafana = Server("Galaxy")
        nginx_grafana = Nginx("Nginx")

    with Cluster("Initialising telegraf"):
        j_c = Jenkins("Jenkins")
        git_c = Github("Infrastructure")
        bash_c = Bash("install custom scripts\n" "install plugin\n " "install telegraf")
        ans_C = Ansible("Ansible")
    j_c >> git_c >> ans_C >> bash_c >> Logging

    servers_user >>  Logging >> Data_storage >> grafana
    server_grafana >> nginx_grafana >> grafana >> Client("Grafana webserver")
    servers_prod >> Logging
#Jenkins
with Diagram("Managing servers with Jenkins", show=False):

    with Cluster("Jenkins node 1"):
        Isengard = Server("Isengard")
        Isen_jenkins = Jenkins("Jenkins all servers")
        Isengard >> Isen_jenkins
    with Cluster("Jenkins node 2"):
        Galaxy = Server("Galaxy")
        Gal_jenkins = Jenkins("Jenkins Galaxy & Cocalc")
        Galaxy >> Gal_jenkins

    with Cluster("User Servers"):
        git_clone_1 = Github("Infrastructure")
        Isengard = Server("Isengard")
        Erebor = Server("Erebor")
        Asgard = Server("Asgard")
        Midgard = Server("Midgard")
        Avans_ans = Ansible("Avans playbook")

    with Cluster("Production Server Galaxy"):
        git_clone_2 = Github("Infrastructure")
        Galaxy_1 = Server("Galaxy")
        Galaxy_test = Server("Test Galaxy")
        Galaxy_ans = Ansible("Galaxy playbook")
        Avans_ans_Gal = Ansible("Avans playbook")


    with Cluster("Production Server Cocalc"):
        git_clone_3 = Github("Infrastructure")
        Avans_ans_Cocalc = Ansible("Avans playbook")


        Cocalc = Server("Cocalc")
        cocalc_ans = Ansible("Cocalc playbook")

    Gal_jenkins >> Cocalc >> git_clone_3 >> cocalc_ans >> Bash("managing Cocalc")
    git_clone_3 >> Avans_ans_Cocalc >> Bash("managing monitoring\n managing users \n installing software")

    Gal_jenkins >> Galaxy_1 >> git_clone_2 >> Galaxy_ans >> Bash("managing installing Galaxy\n"
                                                                 "Installing Tools\n"
                                                                 "Monitoring jobs\n"
                                                                 "Administrating galaxy tasks\n"
                                                                 "Managing Tiaas server")
    Gal_jenkins >> Galaxy_test >> git_clone_2 >> Avans_ans_Gal >> Bash("managing monitoring\n managing users \n installing software")

    Isen_jenkins >> Isengard >> git_clone_1 >> Avans_ans >> Bash("managing monitoring\n managing users \n installing software \n installing backup system \n administrating regular tasks")
    Isen_jenkins >> Erebor  >> git_clone_1
    Isen_jenkins >> Asgard >> git_clone_1
    Isen_jenkins >> Midgard >> git_clone_1
    #Isen_jenkins >> Cocalc >> git_clone_1
    #Isen_jenkins >> Galaxy_1 >> git_clone_1
    #Isen_jenkins >> Galaxy_test >> git_clone_1

with Diagram("Backup system",show=False):


    system_d = Bash("Setting up SystemD, Borg Backup")
    with Cluster("Initialising backup system"):
        Server("Isengard") >> Jenkins("Jenkins all servers") >> Github("Infrastructure") >> system_d

    with Cluster("Backup Protocol weekly"):

        with Cluster("Server projects to be backupped"):
            Isengard = Server("Isengard")
            Asgard = Server("Asgard")
            Midgard = Server("Midgard")

        with Cluster("Backup location"):
            with Cluster("Local"):
                Midgard_B = Server("Midgard_backup")
                Asgard_B = Server("Asgard_backup")
                Isengard_B = Server("Isengard_backup")

            with Cluster("Online"):
                Surf = Server("Surf_backup")

        with Cluster("Monitoring backup logs"):
            Logging = Loki("Telegraf")

        system_d >> Isengard >> Asgard_B
        system_d >> Asgard >> Midgard_B
        system_d >> Midgard >> Isengard_B
        Isengard >> Surf
        Asgard >> Surf
        Midgard >> Surf
        system_d >> Logging
        #Asgard >> Logging
        #Midgard >> Logging
