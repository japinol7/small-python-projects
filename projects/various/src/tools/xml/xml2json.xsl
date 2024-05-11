<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text"/>
    <xsl:strip-space elements="*"/>

    <xsl:template match="*">
        <xsl:if test="position() != 1">,</xsl:if>
        <xsl:value-of select="concat('{&quot;',
      local-name(),
      '&quot;: ')"/>
        <xsl:choose>
            <xsl:when test="count(node()) > 1">
                <xsl:text>[</xsl:text>
                <xsl:apply-templates/>
                <xsl:text>]</xsl:text>
            </xsl:when>
            <xsl:otherwise>
                <xsl:apply-templates/>
            </xsl:otherwise>
        </xsl:choose>
        <xsl:text>}</xsl:text>
    </xsl:template>

    <xsl:template match="text()">
        <xsl:if test="position() != 1">,</xsl:if>
        <xsl:value-of select="concat('{&quot;text&quot;: &quot;',
      normalize-space(),
      '&quot;}')"/>
    </xsl:template>

</xsl:stylesheet>
