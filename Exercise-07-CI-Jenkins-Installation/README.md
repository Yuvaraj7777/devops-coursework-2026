# Exercise 7: Introduction to Continuous Integration (CI) and Jenkins Installation

## 1. Continuous Integration (CI)

Continuous Integration is a development practice where developers frequently integrate code changes into a shared repository. Its goal is to detect errors early, improve software quality, and accelerate delivery.

## 2. Key Features of CI

1. **Frequent Code Integration:** Developers regularly commit code to a shared repository.
2. **Automated Builds:** Builds verify integrated code changes.
3. **Automated Testing:** Tests check that existing functionality continues to work.
4. **Immediate Feedback:** Developers receive quick feedback about failures.

## 3. Benefits of CI

- Early bug detection
- Improved collaboration
- Faster development cycles
- Higher software quality

## 4. How CI Works

1. A developer writes code and pushes it to a version-control repository.
2. A CI server detects or receives the changes.
3. The server builds the code and resolves dependencies.
4. Automated tests validate the changes.
5. Results are communicated to developers.

## 5. Examples of CI/CD Tools

- GitLab CI/CD
- CircleCI
- Travis CI
- Bamboo
- TeamCity
- Azure DevOps Pipelines
- GitHub Actions
- Spinnaker
- Buildkite
- Drone

## 6. Introduction to Jenkins

Jenkins is an open-source automation server used to automate software building, testing, and deployment. It supports Continuous Integration and Continuous Delivery.

### Why Use Jenkins?

- Automates repetitive tasks
- Supports Continuous Integration
- Extends functionality through plugins
- Supports distributed builds across multiple machines

### Key Jenkins Concepts

1. **Job/Project:** A task or process Jenkins executes.
2. **Build:** An execution of a job.
3. **Pipeline:** A sequence of build, test, and deployment steps.
4. **Plugins:** Extensions that add functionality.
5. **Nodes:** Machines where Jenkins jobs execute.

## 7. Jenkins Installation Using Docker

The lab specifies this command:

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
```

The existing Jenkins container was reused rather than creating a duplicate.

- Port 8080 provides access to the Jenkins web interface.
- Port 50000 is used for inbound agent communication.

## 8. Verification

Check the container status with `docker ps -a`.

The existing Jenkins container was verified as running with port 8080 mapped to the host.

Access Jenkins at http://localhost:8080.

## 9. Evidence

See `evidence/Jenkins_dashboard.png` for the Jenkins dashboard screenshot.
