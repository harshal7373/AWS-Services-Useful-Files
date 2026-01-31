package com.awsec2;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.DetachVolumeRequest;
import software.amazon.awssdk.services.ec2.model.DetachVolumeResponse;
import software.amazon.awssdk.services.ec2.model.Ec2Exception;

public class DetachVolume {
    public static void main(String[] args) {
        Region region = Region.AP_SOUTH_1;
        Ec2Client ec2 = Ec2Client.builder()
                .region(region)
                .build();

        String volumeId = "vol-0740f972dcc258660"; // Replace with your volume ID

        try {
            detachEbsVolume(ec2, volumeId);
            System.out.println("Successfully detached volume " + volumeId);
        } catch (Ec2Exception e) {
            e.printStackTrace();
            System.err.println(e.awsErrorDetails().errorMessage());
        } finally {
            ec2.close();
        }
    }

    public static void detachEbsVolume(Ec2Client ec2, String volumeId) {
        DetachVolumeRequest detachRequest = DetachVolumeRequest.builder()
                .volumeId(volumeId)
                .build();

        DetachVolumeResponse detachResponse = ec2.detachVolume(detachRequest);
        System.out.println("Detachment State: " + detachResponse.state());
    }
}
