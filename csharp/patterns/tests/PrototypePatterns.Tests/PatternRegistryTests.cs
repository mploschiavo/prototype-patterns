using PrototypePatterns;

namespace PrototypePatterns.Tests;

public sealed class PatternRegistryTests
{
    [Fact]
    public void RegistryListsAllPatterns()
    {
        var patterns = PatternRegistry.List();
        Assert.Equal(24, patterns.Count);
        Assert.Equal("singleton", patterns[0].Id);
        Assert.Equal("memento", patterns[^1].Id);
    }

    [Fact]
    public void RegistryRunsSinglePatternWithNormalizedId()
    {
        Assert.True(Assert.IsType<bool>(PatternRegistry.RunPattern("singleton")));

        var chainResult = Assert.IsAssignableFrom<IReadOnlyList<string>>(PatternRegistry.RunPattern("chain of responsibility"));
        Assert.Equal(["team-lead", "manager", "unhandled:4"], chainResult);
    }

    [Fact]
    public void RegistryRunsAllPatterns()
    {
        var results = PatternRegistry.RunAllPatterns();
        Assert.Equal(24, results.Count);
        Assert.True(Assert.IsType<bool>(results["singleton"]));
    }

    [Fact]
    public void RegistryThrowsForUnknownPattern()
    {
        Assert.Throws<ArgumentException>(() => PatternRegistry.RunPattern("no-such-pattern"));
    }
}
