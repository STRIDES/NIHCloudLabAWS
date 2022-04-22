If you try to spin up a GPU and sometimes large CPU machines, you may encounter a quota limit. This is in place to prevent users from accidentally spinning up really expensive resources and burning through their whole budget in a few days. 

If you would like to use a machine with a quota limit, you can follow [these instructions](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html).

Here are some Cloud Lab specific instructions as well.
+ Go to `Services > Service Quotas`
+ Click on `Amazon Elastic Compute Cloud (EC2)`
+ Search `On-Demand`, or whatever instance type you are trying to modify (e.g. Spot etc)
+ Click `Running On-Demand P instances`. You need to request whatever instance family you are trying to run. This can be figured out by visiting the [EC2 instance type page](https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&s_kwcid=AL!4422!3!536392622533!e!!g!!aws%20ec2%20instance%20types&ef_id=Cj0KCQjwgYSTBhDKARIsAB8Kuksn1rVhJBBjVbeIAs0DZx_ral7xl0eW-kL8KgMaMmNH8j7gJ0VHHMgaAnn5EALw_wcB:G:s&s_kwcid=AL!4422!3!536392622533!e!!g!!aws%20ec2%20instance%20types) and looking at the prefix of the instance type. For example, p4d.24xlarge	will be from the P family so you need to request `Running On-Demand P instances` and so on for the other machine types.
+ Click `Request quota increase`
+ The quota value is the number of vCPUs allowed for an instance family, so set it to the max CPUs you expect to use
+ Click `Request`
+ In theory, you should only have to wait a few minutes for everything to be updated on the back end and then you can try and launch the blocked instance type again. In practice, it may take up to 30 minutes, so be patient and keep checking back until the `Applied quota value` is updated
+ If you are still having trouble, please contact STRIDES support
