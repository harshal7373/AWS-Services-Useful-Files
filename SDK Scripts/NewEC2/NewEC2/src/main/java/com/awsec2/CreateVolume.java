package com.awsec2;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.CreateVolumeRequest;
import software.amazon.awssdk.services.ec2.model.CreateVolumeResponse;
import software.amazon.awssdk.services.ec2.model.VolumeType;
import software.amazon.awssdk.services.ec2.model.Ec2Exception;

public class CreateVolume {
    public static void main(String[] args) {
        Region region = Region.AP_SOUTH_1;
        Ec2Client ec2 = Ec2Client.builder()
                .region(region)
                .build();

        try {
            String volumeId = createEbsVolume(ec2);
            System.out.println("Successfully created EBS Volume with ID: " + volumeId);
        } catch (Ec2Exception e) {
            e.printStackTrace();
            System.err.println(e.awsErrorDetails().errorMessage());
        } finally {
            ec2.close();
        }
    }

    public static String createEbsVolume(Ec2Client ec2) {
        CreateVolumeRequest volumeRequest = CreateVolumeRequest.builder()
                .availabilityZone("ap-south-1a")  // Replace with your desired availability zone
                .size(100)  // Size of the volume in GiB
                .volumeType(VolumeType.GP2)  // General Purpose SSD (GP2) type
                .build();

        CreateVolumeResponse volumeResponse = ec2.createVolume(volumeRequest);
        return volumeResponse.volumeId();
    }
}
