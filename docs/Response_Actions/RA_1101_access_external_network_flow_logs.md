| Title                       | Accéder aux journaux de flux du réseau externe         |
|:---------------------------:|:--------------------|
| **ID**                      | RA1101            |
| **Description**             | Assurez-vous d'avoir accès aux journaux de flux réseau de communication externe   |
| **Author**                  | @atc_project        |
| **Creation Date**           | 06.05.2020 |
| **Category**                | Network      |
| **Stage**                   |[RS0001: Preparation](../Response_Stages/RS0001.md)| 
| **References** |<ul><li>[https://en.wikipedia.org/wiki/NetFlow](https://en.wikipedia.org/wiki/NetFlow)</li><li>[https://www.plixer.com/blog/how-accurate-is-sampled-netflow/](https://www.plixer.com/blog/how-accurate-is-sampled-netflow/)</li></ul>|
| **Requirements** |<ul><li>MS_border_firewall</li><li>MS_border_ngfw</li><li>DN_zeek_conn_log</li></ul>|

### Workflow

Assurez-vous qu'il existe une collection de journaux de flux réseau pour la communication externe (des actifs de l'entreprise à Internet) configurée.  
S'il n'y a pas d'option pour le configurer sur un périphérique réseau, vous pouvez installer un logiciel spécial sur chaque point de terminaison et le collecter à partir d'eux.  

Attention :  

- Il existe une fonctionnalité appelée ["NetFlow Sampling"](https://www.plixer.com/blog/how-accurate-is-sampled-netflow/), cela élimine la valeur des journaux de flux réseau pour certaines des tâches, telles que «vérifier si un hôte a communiqué avec une adresse IP externe». Assurez-vous qu'il est désactivé ou que vous avez un autre moyen de collecter les journaux de flux réseau.  
