| Titre                       | Obtenir la possibilité de bloquer un domaine externe         |
|:---------------------------:|:--------------------|
| **ID**                      | RA1113            |
| **Description**             | Make sure you have the ability to block an external domain name from being accessed by corporate assets   |
| **Auteur**                  | @atc_project        |
| **Creation Date**           | 06.05.2020 |
| **Catégorie**                | Network      |
| **Étapes**                   |[RS0001: Préparation](../Response_Stages/RS0001.md)| 
| **References** |<ul><li>[https://en.wikipedia.org/wiki/DNS_sinkhole](https://en.wikipedia.org/wiki/DNS_sinkhole)</li></ul>|
| **Requirements** |<ul><li>MS_border_proxy</li><li>MS_border_ips</li><li>MS_border_ngfw</li><li>MS_dns_server</li></ul>|

### Workflow

Make sure you have the ability to create a policy rule or a specific configuration in one of the listed Mitigation Systems that will you to block an external domain name from being accessed by corporate assets.  

Warning:  

- Make sure that using the listed systems (1 or multiple) you can control access to the internet of all assets in the infrastructure. In some cases, you will need a guaranteed way to block an external domain name from being accessed by corporate assets completely. If some of the assets are not under the management of the listed Mitigation Systems, (so they can access the internet bypassing these systems), you will not be able to fully achieve the final objective of the Response Action.  
