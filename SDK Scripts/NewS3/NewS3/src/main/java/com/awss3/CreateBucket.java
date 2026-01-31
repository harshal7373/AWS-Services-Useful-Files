package com.awss3;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.CreateBucketRequest;
import software.amazon.awssdk.services.s3.model.CreateBucketResponse;
import software.amazon.awssdk.services.s3.model.S3Exception;

public class CreateBucket {
    public static void main(String[] args) {
        Region region = Region.AP_SOUTH_1;
        S3Client s3 = S3Client.builder().region(region).build();

        String bucketName = "bucket-7373"; // Replace with your bucket name

        try {
            CreateBucketRequest createBucketRequest = CreateBucketRequest.builder()
                    .bucket(bucketName)
                    .build();

            CreateBucketResponse createBucketResponse = s3.createBucket(createBucketRequest);
            System.out.println("Bucket created: " + createBucketResponse.location());
        } catch (S3Exception e) {
            e.printStackTrace();
            System.err.println(e.awsErrorDetails().errorMessage());
        } finally {
            s3.close();
        }
    }
}
