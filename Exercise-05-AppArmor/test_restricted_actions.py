import docker

client = docker.from_env()

IMAGE_NAME = "flask-apparmor"
PROFILE_NAME = "my-apparmor-profile"
CONTAINER_NAME = "apparmor-test"

print("Starting container with AppArmor profile...")

container = client.containers.run(
    IMAGE_NAME,
    name=CONTAINER_NAME,
    security_opt=[f"apparmor={PROFILE_NAME}"],
    detach=True
)

try:
    container.reload()
    print(f"Container status: {container.status}")

    tests = [
        ("Read /etc/passwd", ["cat", "/etc/passwd"]),
        ("Execute a shell command", ["/bin/sh", "-c", "echo shell-execution-allowed"]),
    ]

    for description, command in tests:
        result = container.exec_run(command)
        print(f"\nTest: {description}")
        print(f"Exit code: {result.exit_code}")
        print(result.output.decode(errors="replace"))

finally:
    print("\nRemoving test container...")
    container.remove(force=True)
    print("Cleanup complete.")