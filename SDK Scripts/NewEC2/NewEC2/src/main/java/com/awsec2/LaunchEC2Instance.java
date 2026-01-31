package com.awsec2;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.RunInstancesRequest;
import software.amazon.awssdk.services.ec2.model.RunInstancesResponse;
import software.amazon.awssdk.services.ec2.model.Tag;
import software.amazon.awssdk.services.ec2.model.TagSpecification;
import software.amazon.awssdk.services.ec2.model.InstanceType;
import software.amazon.awssdk.services.ec2.model.Ec2Exception;

public class LaunchEC2Instance {
    public static void main(String[] args) {
        Region region = Region.AP_SOUTH_1;
        Ec2Client ec2 = Ec2Client.builder()
                .region(region)
                .build();

        try {
            String instanceId = launchEC2Instance(ec2);
            System.out.println("Successfully launched EC2 Instance with ID: " + instanceId);
        } catch (Ec2Exception e) {
            e.printStackTrace();
            System.err.println(e.awsErrorDetails().errorMessage());
        } finally {
            ec2.close();
        }
    }

    public static String launchEC2Instance(Ec2Client ec2) {
        RunInstancesRequest runRequest = RunInstancesRequest.builder()
                .instanceType(InstanceType.T3_MICRO)
                .imageId("ami-0bca660a856fc8c72")  // Replace with your desired AMI ID
                .maxCount(1)
                .minCount(1)
                .keyName("WINDOWS-KP")// Replace with your key pair name
                .securityGroupIds("sg-0d00ae22b6623089b") // Replace with your Security Group Name
                .tagSpecifications(TagSpecification.builder()
                        .resourceType("instance")
                        .tags(Tag.builder()
                                .key("Name")
                                .value("MyEC2Instance")
                                .build())
                        .build())
                .build();

        RunInstancesResponse response = ec2.runInstances(runRequest);
        return response.instances().get(0).instanceId();
    }
}
