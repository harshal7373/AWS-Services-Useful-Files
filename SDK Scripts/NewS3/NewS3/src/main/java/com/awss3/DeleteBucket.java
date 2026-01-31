package com.awss3;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.DeleteBucketRequest;
import software.amazon.awssdk.services.s3.model.S3Exception;

public class DeleteBucket {
    public static void main(String[] args) {
        Region region = Region.AP_SOUTH_1;
        S3Client s3 = S3Client.builder().region(region).build();

        String bucketName = "bucket1876"; // Replace with your bucket name

        try {
            DeleteBucketRequest deleteBucketRequest = DeleteBucketRequest.builder()
                    .bucket(bucketName)
                    .build();

            s3.deleteBucket(deleteBucketRequest);
            System.out.println("Bucket deleted: " + bucketName);
        } catch (S3Exception e) {
            e.printStackTrace();
            System.err.println(e.awsErrorDetails().errorMessage());
        } finally {
            s3.close();
        }
    }
}
