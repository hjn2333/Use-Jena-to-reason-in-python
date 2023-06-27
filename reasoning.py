# @time: 2023/6/9 15:35
# @Author:hjn

import jpype


def reason(jar_path, class_name, func_name, jvm_path="C:/Program Files/Java/jdk-17.0.1/bin/server/jvm.dll"):
    #
    # if jvm_path:
    #     jvmpath = jvm_path
    # else:
    #     jvmpath = jpype.getDefaultJVMPath()
    #
    # jarpath1 = "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/httpcore-4.4.16.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jackson-annotations-2.14.2.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jackson-core-2.14.2.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jackson-databind-2.14.2.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jakarta.json-2.0.1.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jcl-over-slf4j-1.7.36.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-arq-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-base-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-cmds-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-core-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-dboe-base-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-dboe-index-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-dboe-storage-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-dboe-transaction-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-dboe-trans-data-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-iri-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-rdfconnection-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-rdfpatch-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-shacl-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-shaded-guava-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-shex-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-tdb2-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jena-tdb-4.8.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/jsonld-java-0.13.4.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/libthrift-0.18.1.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/log4j-api-2.20.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/log4j-core-2.20.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/log4j-slf4j-impl-2.20.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/protobuf-java-3.22.2.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/slf4j-api-1.7.36.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/titanium-json-ld-1.3.2.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/collection-0.7.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/commons-cli-1.5.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/commons-codec-1.15.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/commons-compress-1.23.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/commons-csv-1.10.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/commons-io-2.11.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/commons-lang3-3.12.0.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/gson-2.10.1.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/httpclient-4.5.14.jar;" \
    #            "D:/Jena/apache-jena-4.8.0/apache-jena-4.8.0/lib/httpclient-cache-4.5.14.jar;"
    # try:
    #     jpype.startJVM(jvmpath, "-ea", "-Djava.class.path=%s;%s" % (jar_path, jarpath1))
    # except Exception as e:
    #     print(str(e))
    java_class = jpype.JClass(class_name)
    java_object = java_class()
    res = eval(f"java_object.{func_name}()")
    # jpype.shutdownJVM()
    return res


