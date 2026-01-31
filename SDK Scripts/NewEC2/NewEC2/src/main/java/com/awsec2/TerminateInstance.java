package com.awsec2;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.TerminateInstancesRequest;
import software.amazon.awssdk.services.ec2.model.TerminateInstancesResponse;
import software.amazon.awssdk.services.ec2.model.Ec2Exception;

public class TerminateInstance {
	public static void main(String[] args) {
		Region region = Region.AP_SOUTH_1;
		Ec2Client ec2 = Ec2Client.builder().region(region).build();

		String instanceId = "i-0ef6314003bc35880"; // Replace with your instance ID

		try {
			terminateEC2Instance(ec2, instanceId);
			System.out.println("Successfully terminated instance " + instanceId);
		} catch (Ec2Exception e) {
			e.printStackTrace();
			System.err.println(e.awsErrorDetails().errorMessage());
		} finally {
			ec2.close();
		}
	}

	public static void terminateEC2Instance(Ec2Client ec2, String instanceId) {
		TerminateInstancesRequest terminateRequest = TerminateInstancesRequest.builder().instanceIds(instanceId)
				.build();

		TerminateInstancesResponse terminateResponse = ec2.terminateInstances(terminateRequest);
		System.out
				.println("Termination State: " + terminateResponse.terminatingInstances().get(0).currentState().name());
	}
}
