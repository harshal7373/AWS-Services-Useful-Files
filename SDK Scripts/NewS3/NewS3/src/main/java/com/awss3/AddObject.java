package com.awss3;

import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;
import software.amazon.awssdk.services.s3.model.PutObjectResponse;
import software.amazon.awssdk.services.s3.model.S3Exception;

import java.nio.file.Paths;

public class AddObject {
    public static void main(String[] args) {
        Region region = Region.AP_SOUTH_1;
        S3Client s3 = S3Client.builder().region(region).build();

        String bucketName = "bucket-7373"; // Replace with your bucket name
        String objectKey = "key2";  // Replace with your object key
        String filePath = "C:\\Users\\Harshal\\Desktop\\about.html"; // Replace with the path to your file

        try {
            PutObjectRequest putObjectRequest = PutObjectRequest.builder()
                    .bucket(bucketName)
                    .key(objectKey)
                    .build();

            PutObjectResponse putObjectResponse = s3.putObject(putObjectRequest,
                    RequestBody.fromFile(Paths.get(filePath)));

            System.out.println("Object uploaded: " + putObjectResponse.eTag());
        } catch (S3Exception e) {
            e.printStackTrace();
            System.err.println(e.awsErrorDetails().errorMessage());
        } finally {
            s3.close();
        }
    }
}
