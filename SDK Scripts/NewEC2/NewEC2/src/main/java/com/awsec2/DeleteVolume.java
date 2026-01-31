package com.awsec2;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.DeleteVolumeRequest;
import software.amazon.awssdk.services.ec2.model.DeleteVolumeResponse;
import software.amazon.awssdk.services.ec2.model.Ec2Exception;

public class DeleteVolume {
    public static void main(String[] args) {
        Region region = Region.AP_SOUTH_1;
        Ec2Client ec2 = Ec2Client.builder()
                .region(region)
                .build();

        String volumeId = "vol-072522db6fcf9091c"; // Replace with your volume ID

        try {
            deleteEbsVolume(ec2, volumeId);
            System.out.println("Successfully deleted volume " + volumeId);
        } catch (Ec2Exception e) {
            e.printStackTrace();
            System.err.println(e.awsErrorDetails().errorMessage());
        } finally {
            ec2.close();
        }
    }

    public static void deleteEbsVolume(Ec2Client ec2, String volumeId) {
        DeleteVolumeRequest deleteRequest = DeleteVolumeRequest.builder()
                .volumeId(volumeId)
                .build();

        DeleteVolumeResponse deleteResponse = ec2.deleteVolume(deleteRequest);
        System.out.println("Volume " + volumeId + " has been deleted.");
    }
}
