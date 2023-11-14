# **A Guide to Writing the NeurIPS Impact Statement | by Centre for the Governance of AI | Medium**

*Carolyn Ashurst, Markus Anderljung, Carina Prunkl, Jan Leike, Yarin Gal, Toby Shevlane, Allan Dafoe*

From improved disease screening to authoritarian surveillance, ML advances will have positive and negative social impacts. Policymakers are struggling to understand these advances, to build policies that amplify the benefits and mitigate the risks. ML researchers need to be part of this conversation: to help anticipate novel ML *applications*, assess the social *implications*, and promote *initiatives* to steer research and society in beneficial directions.

Innovating in this respect, NeurIPS has [introduced a requirement](https://medium.com/@NeurIPSConf/getting-started-with-neurips-2020-e350f9b39c28) that all paper submissions include a statement of the “potential broader impact of their work, including its ethical aspects and future societal consequences.” This is an exciting innovation in scientifically informed governance of technology ([Hecht et al 2018](https://acm-fca.org/2018/03/29/negativeimpacts/) & [Hecht 2020](https://medium.com/@BrentH/suggestions-for-writing-neurips-2020-broader-impacts-statements-121da1b765bf)). It is also an opportunity for authors to think about and better explain the motivation and context for their research to other scientists.

Over time, the exercise of assessing impact could enhance the ML community’s expertise in technology governance, and otherwise help build bridges to other researchers and policymakers. Doing this well, however, will be a challenge. To help maximize the chances of success, we — a team of AI governance, AI ethics, and machine learning (ML) researchers — have compiled some suggestions and [an (unofficial) guide](https://medium.com/@GovAI/a-guide-to-writing-the-neurips-impact-statement-4293b723f832#624f) for how to do this.

# Suggestions

**Highlight both benefits and risks from your research.** The NeurIPS requirement asks that “Authors should take care to discuss both positive and negative outcomes.” Systematically doing so will help us push through the various biases, personal and institutional, towards overly positive or overly negative assessments; after all, few scientific advances are exclusively one or the other. This will also focus attention on the reasons why an advance could be positive or negative, and opportunities for steering developments in more positive directions.

**Highlight uncertainties.** Foreseeing the impacts of research, especially basic research, is notoriously difficult. We recommend acknowledging your uncertainties, while also not letting it stop you from reflecting about impact. This will let others know where they can add more research and how to interpret your statement.

**Focus on tractable, neglected, and significant impacts.** Scientific research tends to have a bewildering array of potential impacts, more so as the research is more foundational or the considered impacts are more long term. It will be infeasible to consider them all.

- Instead, you might deliberately limit the scope of your assessment to those implications that are especially *tractable* to analyze, such as the most obvious direct effects of the advance. You could focus on those implications for which your expertise is especially relevant, for which you have a *comparative advantage*.
- You could focus on those impacts that tend to be *neglected*. It would be more productive for researchers to cover the space of potential impacts of, say, vision systems, than for everyone to discuss, at the same level of detail, the most obvious, such as the well known risk of abuse of surveillance systems.
- You could focus on impacts that would be especially *significant*, even if more speculative, such as applications that could undermine or strengthen public deliberation in democracy.

If you do deliberately limit your focus, you can explicitly note this and why. You could also acknowledge the other main branches of the potential impacts tree that you have chosen to not consider.

**Integrate with your introduction.** From working on your introduction, you probably have already thought through several important impacts of your research, and may have produced relevant text. The impact statement is not just a “detour” from producing a scientific publication, but an opportunity to think more about how to motivate your research, and additional space in which to do so.

**Discuss, read, reflect.** Time permitting, impact assessment will benefit from broad intellectual reflection. Discuss the potential impacts of your research with your colleagues and other thoughtful people. Follow public discussions about technology; read case studies of AI and technology impacts; [read the scholarly literature on tech governance](https://medium.com/@GovAI/a-guide-to-writing-the-neurips-impact-statement-4293b723f832#005f). Boldly ask of your research program: *[what if we succeed?](http://aima.cs.berkeley.edu/)*

**Think about impacts even for theoretical work.** The NeurIPS organisers [have stated](https://neurips.cc/Conferences/2020/PaperInformation/NeurIPS-FAQ) that authors of very theoretical or general research can write that “a Broader Impact discussion is not applicable.” Yet, theoretical work does have downstream impact — that’s after all a motivation for much theoretical work — and so we encourage researchers to make an attempt, perhaps reflecting on their subfield more broadly.

**Build supporting structure for impact assessment.** Build impact assessment into your intellectual habits. If you can shape a research group or institution, build supporting structures to encourage this: allocate time in group conversations, recognize and reward exemplary contributions, perhaps build a researcher-led institutional review process. Concretely for NeurIPS 2020, while your impact statement must be included with the full paper submission on June 3, you can take advantage of the later deadline for supplementary materials to elaborate on your impact assessment.

# A Guide: Applications, Implications, Initiatives

To guide an impact assessment, you can ask yourself three questions:

**Q1 — Applications — How could your research affect ML applications?
 Q2 — Implications — What are the societal implications of these applications?
 Q3 — Initiatives — What research or other initiatives could improve societal outcomes?**

We organize the first two questions using the *Impact Stack*.

At the base is foundational research, which feeds upwards into research on ML techniques. Q1 asks how research in these layers affect ML applications*.* Q2 asks how these applications lead to real-world uses, such as by business and governments, and what the societal impacts of those uses are. Finally, Q3 steps outside of the stack, and asks what else we could do to mitigate risks and maximize benefits, such as through research or by innovating in norms, policies, institutions, and best practices.

We now walk through these questions more systematically.

**Map your research to the stack**Identify where your contribution fits in the Impact Stack, and what major impacts it has on other layers. For example, the introduction of benchmarks or software tools might speed progress in particular techniques (layer 1) or applications (layer 2); neuroscience models of the brain might provide insights for optimization (layer 0) or neural network architectures (layer 1).

**Q1. APPLICATIONS — How could your research affect ML applications?**

Consider how the impact of your research branches through the stack to *ML applications,* which refer to tools and solutions for particular tasks. These could be broad, such as image classification, or more narrow, such as lip-reading. You could consider:

- **Existing applications** your research contributes towards, clarifying how it does so. E.g. in improving transformers your research may improve various NLP applications.
- **New applications** that are made possible by your research, clarifying how it does so.
- **Properties of applications** that might be affected by your research. Consider how ML applications that use your insights might be different from other applications. Increases in interpretability, sample efficiency, and accuracy will all have different downstream effects.
- **Ethical considerations relating to your research process**, such as whether your data has privacy or fairness issues.
- For more prompts, see [A — Properties](https://medium.com/@GovAI/a-guide-to-writing-the-neurips-impact-statement-4293b723f832#bee2) below.

**Q2. IMPLICATIONS — What are the societal implications of these applications?**

Based on your answers to Q1, what are the possible uses of these applications outside of the lab? For example, a lip-reading tool could be used to transcribe CCTV footage for evidence in a lawsuit. You could consider:

- **Possible uses**, by different entities (e.g. different industries, governments, individuals), for different purposes. Consider the full range of uses, particularly novel ones and those by actors with varying intentions — malicious, benign, and benevolent.
- **The range of societal impacts** resulting from these uses. Think about various groups of people (different end users, companies, industries, governments). Think about both *intended and unintended effects*, *immediate and long term effects*. In thinking through potential risks, you can consider [accidents, malicious uses, and structural risks](https://www.lawfareblog.com/thinking-about-risks-ai-accidents-misuse-and-structure).
- **Impacts from significant properties** that you have identified. In particular, consider the impacts from the errors and limitations you identified (e.g. with privacy, fairness, transparency).
- See also [A — Properties](https://medium.com/@GovAI/a-guide-to-writing-the-neurips-impact-statement-4293b723f832#bee2), [B —Application owners and users](https://medium.com/@GovAI/a-guide-to-writing-the-neurips-impact-statement-4293b723f832#1b57) and [C — Types of societal impact](https://medium.com/@GovAI/a-guide-to-writing-the-neurips-impact-statement-4293b723f832#1f29) below.

**Q3. INITIATIVES — What research or other initiatives could improve societal outcomes?**

What work could be done to increase the positive impacts and reduce the downsides? These could include:

- **ML research suggestions**, such as ideas for research into *beneficial applications, improving understanding of risks,* or *technical mitigations*, such as diagnostic tools or strategies to make algorithms more robust.
- **Suggestions for research beyond ML**, such as in psychology, economics, political science, philosophy and more. Your thinking may illuminate new technical possibilities, for which we need more social research to understand the implications, and to devise non-technical mechanisms for mitigation.
- **Other initiatives,** including suggestions for how other kinds of actors, such as *firms, policymakers, educators, regulators,* and *the media,* can respond to the possibilities arising from this research.

Below, we provide some additional resources that can help you write your statement: a set of example statements and some additional prompts and resources.

# Suggestions for example statements

Here we include three example impact statements written using the above guide. For brevity we include a subset of the considerations that could be included. We encourage authors to, if time allows, include a greater depth of explanation and discussion where they are able to, in particular regarding the specifics of their own research.

## GNNExplainer — Generating Explanations for Graph Neural Networks

*In [this paper](https://papers.nips.cc/paper/9123-gnnexplainer-generating-explanations-for-graph-neural-networks.pdf), the authors introduce GNNExplainer, a model-agnostic approach for providing explanations for predictions of Graph Neural Network (GNN)-based models.*

GNNs (and hence GNNExplainer) could be applied to a wide range of applications, including computer vision, natural language processing, recommender systems, traffic prediction, generative models and many more ([Zhou et al 2019](https://arxiv.org/pdf/1812.08434.pdf), [Wu et al 2019](https://arxiv.org/pdf/1901.00596.pdf)). Our research could be used to provide explanations for GNNs in these applications, improving understanding of individual decisions, as well as the underlying models.

While there will be important impacts resulting from the use of GNNs in general, here we focus on the impact of using our tool to provide explanations for such systems. There are many benefits to using such a tool, such as increasing the transparency in decision-critical applications. This can help mitigate fairness, privacy and safety risks — see the introduction of [the paper](https://papers.nips.cc/paper/9123-gnnexplainer-generating-explanations-for-graph-neural-networks.pdf) for more details. The potential risks of increasing explainability have typically received less attention. These include: (i) the risk of [automation bias](https://www.tandfonline.com/doi/abs/10.1207/s15327108ijap0801_3), i.e. an undue trust in models (see e.g. [PAI 2019](https://www.partnershiponai.org/human-ai-collaboration-trust-literature-review-key-insights-and-bibliography/)), (ii) if the use of explanations means systems may now be used by those with lower levels of domain or ML expertise, this could increase the risk of the model or its outputs being used incorrectly, (iii) if explanations are only used during the development phase, and the model is retrained over time, changing its behaviour, this could again lead to a false sense of security.

We see opportunities for research applying GNNExplainer to beneficial purposes, such as investigating whether GNNExplainer could improve algorithmic fairness. To mitigate the risks associated with using generated explanations, we encourage research to understand the impacts of using GNNExplainer in particular real-world scenarios. In these scenarios, do users understand the explanations given, and act accordingly, not falling prey to automation bias? Does use of the system improve or diminish domain expertise over time?

## SuperGLUE — An NLP benchmark

*In [this paper](https://arxiv.org/pdf/1905.00537.pdf), researchers introduce SuperGLUE, a benchmark and leaderboard for General-Purpose Language Understanding Systems.*

Our benchmark is likely to increase progress of NLP applications and, like [GLUE](https://arxiv.org/abs/1804.07461), drive the development of general-purpose language systems. Such systems may be able to complete a wide range of tasks: from question-answering and sentiment analysis to [poetry](https://www.gwern.net/GPT-2) and [role-playing games](https://aidungeon.io/).

The NLP systems whose development is spurred and supported by our benchmark may contribute to a large range of uses, including customer services, helpdesks, retail and sales, healthcare services, financial and legal services, and marketing. Each of these uses may have a broad range of societal implications: The use of dialogue systems in place of help-desks could bring benefits such as cost savings and removing repetitive tasks, but could also result in job losses. Personal assistants in smart home devices could increase autonomy for the elderly, while also raising questions about the [reinforcement of gender norms](https://www.tandfonline.com/doi/full/10.1080/15295036.2018.1488082?journalCode=rcsm20), the collection of personal data, and the risk of hackers accessing private information. Of particular concern is the use of NLP models by those wishing to spread misinformation or create an information environment of uncertainty and mistrust (see [discussions around the staged release of GPT-2](https://openai.com/blog/gpt-2-6-month-follow-up/)).

There are also important considerations relating to benchmarks themselves. Any widely used benchmark may skew research in a certain direction. For example, our benchmark may bias research in favour of approaches that work particularly well for English. Models trained on biased datasets may inherit those biases. For example, gender bias may be one such concern. To mitigate this risk, we included the analysis tool Winogender to give some indication of whether the models display gender bias.

We would encourage further work to understand the biases and limitations of the datasets used in SuperGLUE. We would also suggest that other benchmarks follow suit by including analysis tools to detect gender bias and other limitations. We encourage researchers to develop NLP systems for tasks we can expect to be particularly beneficial, such as text-based counselling.

We also encourage research to understand and mitigate the risks arising from NLP applications. With regards to the risks of machine-generated misinformation, a short-term solution may be developing detection systems. However, we expect such detection systems to become ineffectual as NLP improves. Therefore, we recommend researchers and policymakers look into how platforms can detect and stop the spread of *harmful* content, as opposed to *machine-generated* content.

## Pluribus — Superhuman AI for multiplayer poker

*In [this paper](https://science.sciencemag.org/content/365/6456/885?hwshib2=authn%3A1586430826%3A20200408%253A56334cfe-9c1f-4898-b446-faf5396f1d1a%3A0%3A0%3A0%3A43HWIvGbDij4N0foTHhZnw%3D%3D), researchers introduce Pluribus, a system that can beat the top professional human players in 6-player Texas Hold ’Em poker.*

While we could discuss the impacts of poker playing systems, we have chosen to broaden our focus to consider the longer term impacts of developing strategic capabilities within hidden information settings. Such capabilities could be applied to a range of domains, such as auctions, match-making, scheduling, pricing, and cybersecurity.

Improvements to actors’ skills in hidden information strategic games likely have complex effects on welfare, depending on how these capabilities are distributed and the character of the strategic setting. For example, if the setting is close to zero sum, such as in poker, then any change in skill is only likely to shift value to those whose skill is improved more; depending on who can use this scientific advance, such as criminals or well-motivated citizens, this technology may be socially harmful or beneficial. If access to this capability is mostly available to the wealthy, it could plausibly promote concentration of wealth. If the setting is one where there are opportunities for Pareto improvements, such as in trade negotiations, then plausibly increased skill could increase total welfare.

We suggest that researchers in social sciences and machine learning investigate questions such as:

- In what additional applications can the insights from this and related research be put to use?
- If this line of research did lead to increased strategic capabilities in particular domains, how will those capabilities be distributed?
- If these capabilities are unevenly distributed, what are the overall welfare effects? What if they are evenly distributed?

# Additional prompts and resources

In this section we provide additional prompts to use with the questions above. We also include references for further reading.

## Background reading

## A — Properties

When thinking about (i) the ethical implications of how you have gone about your research, or (ii) properties/limitations/risks of future systems that build off your research, you may wish to consider the following.

- **Explainability and transparency —** How readily can the system as a whole, or the reasoning for individual decisions/behaviour, be understood? ([Gilpin et al 2019](https://arxiv.org/pdf/1806.00069.pdf), [Doshi-Velez et al 2017](https://arxiv.org/pdf/1702.08608.pdf))
- **Performance metrics —** For the metrics used in your paper — such as accuracy, precision/recall, BLEU score — do they faithfully demonstrate that the method performs as intended? What are the limitations of the metrics used? Why did you choose to use them? How will changes in performance resulting from your research impact downstream uses?
- **Fairness** — Are there biases in the datasets you have used in your research? Could your research be used in future systems that treat certain groups unfairly, or reinforce harmful stereotypes? For example by training on data that contains historic biases, such as biased decisions, or data in which certain groups are not adequately represented. For such systems, what do developers need to do to avoid harmful biases? ([Mehrabi et al 2019](https://arxiv.org/pdf/1908.09635.pdf), [Crawford 2017](https://www.youtube.com/watch?v=fMym_BKWQzk)).
- **Data, memory and compute requirements —** What are the data, memory and compute requirements for training the system, or for the trained system to complete tasks? What restrictions does this put on future uses? What is the environmental impact? ([Tucker et al 2019](https://arxiv.org/abs/2001.05068))
- **Robustness and generalisability —** For future deployed systems, how should developers ensure the system behaves well on data whose distribution differs from the training set? ([Ben-David et al 2010](http://www.alexkulesza.com/pubs/adapt_mlj10.pdf), [Amodei et al 2016](https://arxiv.org/pdf/1606.06565.pdf))
- **Adversarial robustness —** To what extent are your methods robust to adversarial ML attacks, such as data poisoning? ([Kurakin et al 2016](https://arxiv.org/abs/1611.01236))
- **Errors, accidents, failure modes, bias —** What are the possible failure modes? For deployed systems, what effects could result from individual errors or larger failures? ([Microsoft 2019](https://docs.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning))
- **Feedback loops —** For deployed systems, could the outputs of the system bias the inputs to the system in a problematic way? ([Ensign et al 2017](https://arxiv.org/abs/1706.09847))
- **Privacy implications —** For deployed systems, what are the risks around obtaining adequate consent for use of personal data, identifiability of personal data, and information security? Are there privacy concerns regarding the data used in your work? ([Papernot 2018](https://arxiv.org/pdf/1811.01134.pdf), [Al-Rubaie et al 2018](https://arxiv.org/pdf/1804.11238.pdf))

## B — Application owners and users

You may wish to consider the application owners and users below. Different owners and users will have different considerations and needs; some require extremely robust methodology, others require real-time applications, others will require the application to scale.

- Different **industry sectors** such as transport, manufacturing, internet companies, HR, retail, financial services, the media, law. ([McKinsey 2018](https://www.mckinsey.com/featured-insights/artificial-intelligence/notes-from-the-ai-frontier-applications-and-value-of-deep-learning), [Wuerst et al 2016](https://www.tandfonline.com/doi/full/10.1080/21693277.2016.1192517))
- Different **government departments and public services providers** such as health, education, policing, the military. ([OECD 2019](https://oecd-opsi.org/wp-content/uploads/2019/11/AI-Report-Online.pdf))
- Different **researchers, academics and non-profits** for social, environmental or scientific research. ([RoyalSociety 2019a](https://royalsociety.org/-/media/policy/projects/ai-and-society/AI-revolution-in-science.pdf?la=en-GB&hash=5240F21B56364A00053538A0BC29FF5F))
- **Malicious actors** such as cyber-criminals or terrorists. ([Brundage et al 2018](https://arxiv.org/abs/1802.07228))

## C — Types of societal impact

This (nonexhaustive) list can be used as a starting point for anticipating different impacts for a given application.

- **Economic —** The impact on particular industries, overall economic impact, impact on employment opportunities and the nature of work ([Frey et al 2013](https://www.oxfordmartin.ox.ac.uk/downloads/academic/future-of-employment.pdf))
- **Environmental —** The environmental impact of training ML systems, and of the use of ML systems. Applications that can be used to model environmental concerns ([Rolnick et al 2019](https://arxiv.org/abs/1906.05433), [AI Now 2019](https://medium.com/@AINowInstitute/ai-and-climate-change-how-theyre-connected-and-what-we-can-do-about-it-6aa8d0f5b32c))
- **Equality —** The impact on discrimination and fairness, through differential access or treatment, or reinforcement of existing financial, social, racial or gender inequalities or stereotypes ([Mehrabi et al 2019](https://arxiv.org/pdf/1908.09635.pdf), [Corbett-Davies et al 2018](https://arxiv.org/pdf/1808.00023.pdf), [Crawford 2017](https://www.youtube.com/watch?v=fMym_BKWQzk))
- **Development —** The impacts from applications that can be used in education, or in support of sustainable development goals ([Vinuesa et al 2020](https://www.nature.com/articles/s41467-019-14108-y))
- **Political —** The impact to politics, democracy, the control and spread of information, privacy, surveillance, weapons ([Bradshaw et al 2018](https://comprop.oii.ox.ac.uk/research/cybertroops2018/), [EC 2020](https://ec.europa.eu/info/sites/info/files/commission-white-paper-artificial-intelligence-feb2020_en.pdf))
- **Products and services —** Impacts resulting from access to improved individualised products and services
- **Science and technology —** The impacts from improvement in applications that can be used in health, science, transport or technology ([RoyalSociety 2019a](https://royalsociety.org/-/media/policy/projects/ai-and-society/AI-revolution-in-science.pdf?la=en-GB&hash=5240F21B56364A00053538A0BC29FF5F), [RoyalSociety 2019b](https://royalsociety.org/-/media/policy/Publications/2019/29-03-19-ai-in-health-and-care-discussion-notes.pdf?la=en-GB&hash=7C63DD77C08B9FF5B94EF1CE63F69B7A), [Carleo et al 2019](https://arxiv.org/pdf/1903.10563.pdf))

# Acknowledgments

*For discussions and input we thank: Dario Amodei, Miles Brundage, Rosie Campbell, Ryan Carey, Jack Clark, Jeff Ding, Seb Farquhar, Iason Gabriel, Ben Garfinkel, Adam Gleave, Raia Hadsell, Lewis Hammond, Brent Hecht, Jade Leung, Jelena Luketina, Vishal Maini, Sören Mindermann, Joshua Tenenbaum, Aaron Tucker, Jess Whittlestone, and Ben Zevenberger. We’d also like to thank the authors of the papers we used to write example statements.*

# About the authors

*Carolyn Ashurst is a Senior Research Scholar at the Future of Humanity Institute and Research Affiliate at the Centre for the Governance of AI.*

*Markus Anderljung is a Project Manager at the Centre for the Governance of AI, at the Future of Humanity Institute.*

*[Carina Prunkl](https://www.carinaprunkl.com/) is a Senior Research Scholar at the Future of Humanity Institute and Research Affiliate at the Centre for the Governance of AI, University of Oxford.*

*[Yarin Gal](http://www.cs.ox.ac.uk/people/yarin.gal/website/) is an Associate Professor of Machine Learning at the [University of Oxford Computer Science Department](http://www.cs.ox.ac.uk/), and head of the [Oxford Applied and Theoretical Machine Learning Group (OATML)](http://oatml.cs.ox.ac.uk/).*

*Toby Shevlane is a Researcher at the Centre for the Governance of AI and a DPhil student at Oxford’s Faculty of Law (Centre for Socio-Legal Studies).*

*[Allan Dafoe](https://www.allandafoe.com/) is Associate Professor, International Politics of Artificial Intelligence and Director of the Centre for the Governance of AI, at the Future of Humanity Institute, University of Oxford.*

*The Centre for the Governance of AI is based at the Future of Humanity Institute, University of Oxford. For more information, visit: [governance.ai](http://governance.ai/).*

For feedback on the guide, feel free to email: [neuripsimpactstatement@governance.ai](mailto:NeurIPSImpactStatement@governance.ai)

