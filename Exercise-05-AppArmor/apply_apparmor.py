import docker

client = docker.from_env()

IMAGE_NAME = "flask-apparmor"
PROFILE_NAME = "my-apparmor-profile"
CONTAINER_NAME = "apparmor-flask"

print("Building Docker image...")

image, build_logs = client.images.build(
    path=".",
    tag=IMAGE_NAME
)

for entry in build_logs:
    if "stream" in entry:
        print(entry["stream"], end="")

print("\nStarting container with AppArmor profile...")

container = client.containers.run(
    IMAGE_NAME,
    name=CONTAINER_NAME,
    ports={"5000/tcp": 5000},
    security_opt=[f"apparmor={PROFILE_NAME}"],
    detach=True
)

try:
    container.reload()
    print(f"Container ID: {container.short_id}")
    print(f"Container status: {container.status}")

    details = client.api.inspect_container(container.id)
    print("Configured security options:")
    print(details["HostConfig"]["SecurityOpt"])

finally:
    print("Stopping and removing the test container...")
    container.remove(force=True)
    print("Cleanup complete.")