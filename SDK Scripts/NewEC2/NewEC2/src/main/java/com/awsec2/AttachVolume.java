package com.awsec2;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.AttachVolumeRequest;
import software.amazon.awssdk.services.ec2.model.AttachVolumeResponse;
import software.amazon.awssdk.services.ec2.model.Ec2Exception;

public class AttachVolume {
    public static void main(String[] args) {
        Region region = Region.AP_SOUTH_1;
        Ec2Client ec2 = Ec2Client.builder()
                .region(region)
                .build();

        String instanceId = "i-0ff451ca08a35d548"; // Replace with your instance ID
        String volumeId = "vol-072522db6fcf9091c"; // Replace with your volume ID
        String device = "/dev/sdf"; // Replace with your desired device name

        try {
            attachEbsVolume(ec2, instanceId, volumeId, device);
            System.out.println("Successfully attached volume " + volumeId + " to instance " + instanceId);
        } catch (Ec2Exception e) {
            e.printStackTrace();
            System.err.println(e.awsErrorDetails().errorMessage());
        } finally {
            ec2.close();
        }
    }

    public static void attachEbsVolume(Ec2Client ec2, String instanceId, String volumeId, String device) {
        AttachVolumeRequest attachRequest = AttachVolumeRequest.builder()
                .instanceId(instanceId)
                .volumeId(volumeId)
                .device(device)
                .build();

        AttachVolumeResponse attachResponse = ec2.attachVolume(attachRequest);
        System.out.println("Attachment State: " + attachResponse.state());
    }
}
