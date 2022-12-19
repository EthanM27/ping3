FROM fuzzers/atheris:2.0.7-python3.9

RUN pip install ping3
COPY . /ping3
WORKDIR /ping3
RUN chmod +x /ping3/mayhem/fuzzer.py
CMD ["/ping3/mayhem/fuzzer.py"]
