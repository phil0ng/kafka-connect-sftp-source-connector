FROM confluentinc/cp-kafka:5.0.0

COPY kafka-connect-configuration.sh /usr/bin/
COPY *.properties /etc/kafka/
COPY confluentinc-kafka-connect-sftp-2.0.0 /opt/

RUN cd /usr/share/java/kafka && \
    ln -s /opt/lib sftp

CMD ["/usr/bin/kafka-connect-configuration.sh"]