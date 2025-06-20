from setuptools import find_packages, setup

setup(
    name="hotel_booking_agent",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="Himanshu",
    author_email="doshi.hims@gmail.com",
    description="AI Hotel Booking Agent",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/22Himanshu/Hiring_challange",
)
