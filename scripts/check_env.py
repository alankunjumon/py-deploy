import os

required_vars = ["ENV","AWS_REGION"]

missing = []

for var in required_vars:
	if not os.environ.get(var):
		missing.append(var)

if missing:
	print("Missing environment variables", missing)
	exit(1)
else:
	print("All required environment variables are present")
