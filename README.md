To ensure a secure software development lifecycle, we need to implement DevSecOps practices, automating security checks at every stage.

This project aims to:

  1.Use Docker or kubernites for containerization to ensure a consistent and isolated environment.
  2.Implement Aqua Security (Trivy) to scan and mitigate vulnerabilities in container images.
  3.Automate deployment with GitHub Actions, ensuring a smooth CI/CD pipeline with security checks.
  BONUS:
  4. Prepare for AI-based threat monitoring using TensorFlow to detect anomalies in system logs. 

  
1. LOCAL CONTAINER FORMATION:
   in this project we can either use docker or kubernites for creating a container to run oru application,webserver, etc..
   we tried to form both the containers and we used respective AI powered system scanners
   a.DOCKER
        first we created a docker container using vs code terminal and by side we created a front end web server application form
        which enables the user to input username and password and send a particular file . this website is run inside the docker.
        from the repository you can find a docker file where we created our container
   b.KUBERNITES:
        this is another container application where we created a container which contains a application image of a certain file using a request routine nginx.

2.IMPLEMENTING AQUASECURITY FOR SCANNING THE CONTAINER:
        aqua security is a mix of trivy + trained a AI model (using linear regression) for scanning the vulnerabilities in the image that we created.
        we do this by using 3 steps:
        1. scan the container using trivy (signed system scanner) to get the vulnerabilities present and assign them a severity score ranging from (0 to 100)
        2. Use trained ai model using python to analyze vulnerabilities from the JSON file that we created using the output of the trivy scan. 
        3. Logistic Regression is a type of classification algorithm used in machine learning. It predicts the probability of an event occurring, such as
        whether a vulnerability is exploitable (1) or not (0).  
        4.We’ll train a Logistic Regression model to predict whether a vulnerability is exploitable (1) or not (0) based on:
                1.Severity (CRITICAL, HIGH, MEDIUM, LOW)
                2.Package affected
                3.Risk score
        The result is then plotted in a graph based on severity and risck score
        
3.REAL TIME THREAD MONITORING AND AI AUTOMATED SOLUTIONS FOR THE VULNERABILITIES:
 we could have gone for many pre available softwares such as falco. but we thought that would not be that interesting so with the local host that we created (the web application form)
 we made 2 changes in the app.py code
                                 1.if the user attempts to enter wrong password or username for more than 5 times that might be considered as an vulnerability,
                                 2.upon uploading a file in the web application form the image is scanned using the previous steps we find the vulnerabilities present in the file.
to check this we did a brute-force attack on the web application and monitored the "data log sheet" simultaneously. and then found the vulnerabilities.

FLAWS :

1.we couldn't bring a real time large data base so we had to work wiht smaller sample.
2. we couldn't integrate the DevSecOps and complete it and deploy it as a complete software.


  
