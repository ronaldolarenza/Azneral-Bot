# We're using Ubuntu 20.10
FROM koala21/dockerkampang:latest
#
# Clone repo and prepare working directory
#
RUN git clone -b Kampang https://github.com/ManusiaRakitan/Kampang-Bot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ManusiaRakitan/Kampang-Bot/Kampang/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
