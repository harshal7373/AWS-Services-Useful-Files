package com.awss3;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.DeleteObjectRequest;
import software.amazon.awssdk.services.s3.model.DeleteObjectResponse;
import software.amazon.awssdk.services.s3.model.S3Exception;

public class DeleteObject {
    public static void main(String[] args) {
        Region region = Region.AP_SOUTH_1;
        S3Client s3 = S3Client.builder().region(region).build();

        String bucketName = "bucket1876"; // Replace with your bucket name
        String objectKey = "key1";  // Replace with your object key

        try {
            DeleteObjectRequest deleteObjectRequest = DeleteObjectRequest.builder()
                    .bucket(bucketName)
                    .key(objectKey)
                    .build();

            DeleteObjectResponse deleteObjectResponse = s3.deleteObject(deleteObjectRequest);
            System.out.println("Object deleted: " + deleteObjectResponse.deleteMarker());
        } catch (S3Exception e) {
            e.printStackTrace();
            System.err.println(e.awsErrorDetails().errorMessage());
        } finally {
            s3.close();
        }
    }
}
